#!/usr/bin/env python3
"""
구석기 석기 일러스트 SVG 검증 스크립트
Paleolithic Lithic Illustration SVG Validator

국제 관례 기반 표준 준수 자동 검증
"""

import xml.etree.ElementTree as ET
import sys
import re
from pathlib import Path

# 네임스페이스
NS = {
    'svg': 'http://www.w3.org/2000/svg',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
}

# 표준 레이어 (순서대로)
EXPECTED_LAYERS = [
    '01_OUTLINE', '02_SCARS', '03_RIPPLES', '04_CORTEX',
    '05_SECTION', '06_LINKS', '07_SYMBOLS', '08_LABELS',
    '09_LEGEND', '10_GUIDES'
]

# 표준 선굵기 (mm, 허용 오차 ±0.05mm)
STANDARD_WIDTHS = {
    'outline': (0.45, 0.05),
    'scar': (0.30, 0.05),
    'ripple': (0.20, 0.05),
    'linking': (0.15, 0.05),
    'section-outline': (0.45, 0.05),
    'section-hatching': (0.20, 0.05),
}

class LithicValidator:
    def __init__(self, svg_path):
        self.svg_path = Path(svg_path)
        self.tree = None
        self.root = None
        self.errors = []
        self.warnings = []
        self.info = []

    def load_svg(self):
        """SVG 파일 로드"""
        try:
            self.tree = ET.parse(self.svg_path)
            self.root = self.tree.getroot()
            return True
        except Exception as e:
            self.errors.append(f"SVG 파일 로드 실패: {e}")
            return False

    def check_page_size(self):
        """페이지 크기 확인 (A4 또는 A3)"""
        width = self.root.get('width', '')
        height = self.root.get('height', '')

        if width == '210mm' and height == '297mm':
            self.info.append("✓ 페이지 크기: A4 (210×297mm)")
            return True
        elif width == '297mm' and height == '420mm':
            self.info.append("✓ 페이지 크기: A3 (297×420mm)")
            return True
        else:
            self.warnings.append(f"⚠ 비표준 페이지 크기: {width} × {height}")
            return False

    def check_units(self):
        """단위 확인 (mm)"""
        width = self.root.get('width', '')
        height = self.root.get('height', '')

        if 'mm' in width and 'mm' in height:
            self.info.append("✓ 단위: mm")
            return True
        else:
            self.errors.append("✗ 단위가 mm이 아님")
            return False

    def check_layers(self):
        """레이어 구조 확인"""
        layers = self.root.findall('.//svg:g[@inkscape:groupmode="layer"]', NS)
        found_layers = [
            layer.get('{http://www.inkscape.org/namespaces/inkscape}label')
            for layer in layers
        ]

        # 필수 레이어 확인
        missing = [l for l in EXPECTED_LAYERS if l not in found_layers]
        extra = [l for l in found_layers if l not in EXPECTED_LAYERS]

        if not missing:
            self.info.append(f"✓ 레이어: {len(found_layers)}개 모두 존재")
        else:
            self.errors.append(f"✗ 누락된 레이어: {', '.join(missing)}")

        if extra:
            self.warnings.append(f"⚠ 추가 레이어: {', '.join(extra)}")

        return len(missing) == 0

    def check_line_widths(self):
        """선 두께 확인"""
        issues = []

        # 모든 요소의 스타일 확인
        for elem in self.root.iter():
            style = elem.get('style', '')
            stroke_width_match = re.search(r'stroke-width:\s*([\d.]+)(mm|px)?', style)

            if stroke_width_match:
                width_str = stroke_width_match.group(1)
                unit = stroke_width_match.group(2) or ''

                try:
                    width = float(width_str)

                    # mm 단위가 아니면 경고
                    if unit != 'mm' and width > 1:
                        self.warnings.append(f"⚠ 단위 누락 또는 px 사용: {width_str}{unit}")

                    # 표준 범위 확인 (mm 기준)
                    if unit == 'mm' or (unit == '' and width < 1):
                        in_range = False
                        for name, (std, tolerance) in STANDARD_WIDTHS.items():
                            if abs(width - std) <= tolerance:
                                in_range = True
                                break

                        if not in_range:
                            issues.append(f"{width}{unit}")

                except ValueError:
                    pass

        if not issues:
            self.info.append("✓ 선 두께: 표준 범위 준수")
        else:
            self.warnings.append(f"⚠ 비표준 선 두께 발견: {', '.join(set(issues[:5]))}")

        return True

    def check_colors(self):
        """색상 확인 (흑백만 허용)"""
        forbidden_colors = []

        for elem in self.root.iter():
            # stroke 색상 확인
            style = elem.get('style', '')

            # RGB 색상 패턴
            rgb_match = re.search(r'(?:stroke|fill):\s*rgb\((\d+),\s*(\d+),\s*(\d+)\)', style)
            if rgb_match:
                r, g, b = map(int, rgb_match.groups())
                if not (r == g == b):  # 흑백이 아님
                    forbidden_colors.append(f"rgb({r},{g},{b})")

            # HEX 색상 패턴
            hex_match = re.search(r'(?:stroke|fill):\s*#([0-9a-fA-F]{6})', style)
            if hex_match:
                hex_color = hex_match.group(1).lower()
                # 흑백 확인 (RR==GG==BB)
                if hex_color[0:2] != hex_color[2:4] or hex_color[2:4] != hex_color[4:6]:
                    forbidden_colors.append(f"#{hex_color}")

        if not forbidden_colors:
            self.info.append("✓ 색상: 흑백만 사용")
        else:
            self.errors.append(f"✗ 컬러 사용 금지: {', '.join(set(forbidden_colors[:3]))}")

        return len(forbidden_colors) == 0

    def check_guides_layer(self):
        """GUIDES 레이어 숨김 확인"""
        guides_layer = None
        for layer in self.root.findall('.//svg:g[@inkscape:groupmode="layer"]', NS):
            label = layer.get('{http://www.inkscape.org/namespaces/inkscape}label')
            if label == '10_GUIDES':
                guides_layer = layer
                break

        if guides_layer is not None:
            style = guides_layer.get('style', '')
            if 'display:none' in style:
                self.info.append("✓ GUIDES 레이어: 숨김 처리됨 (출력 제외)")
            else:
                self.warnings.append("⚠ GUIDES 레이어가 보이기 상태 (출력 시 숨겨야 함)")

        return True

    def check_metadata(self):
        """메타데이터 확인"""
        title = self.root.find('.//{http://purl.org/dc/elements/1.1/}title')

        if title is not None and title.text:
            self.info.append(f"✓ 메타데이터: 제목 '{title.text[:30]}...'")
        else:
            self.warnings.append("⚠ 메타데이터: 제목 없음")

        return True

    def validate(self):
        """전체 검증 실행"""
        print(f"\n{'='*60}")
        print(f"구석기 석기 일러스트 SVG 검증")
        print(f"{'='*60}\n")
        print(f"파일: {self.svg_path}\n")

        if not self.load_svg():
            self.print_results()
            return False

        # 검증 실행
        self.check_page_size()
        self.check_units()
        self.check_layers()
        self.check_line_widths()
        self.check_colors()
        self.check_guides_layer()
        self.check_metadata()

        self.print_results()

        return len(self.errors) == 0

    def print_results(self):
        """검증 결과 출력"""
        print("검증 결과:")
        print("-" * 60)

        if self.info:
            print("\n정보:")
            for msg in self.info:
                print(f"  {msg}")

        if self.warnings:
            print("\n경고:")
            for msg in self.warnings:
                print(f"  {msg}")

        if self.errors:
            print("\n오류:")
            for msg in self.errors:
                print(f"  {msg}")

        print("\n" + "="*60)

        if not self.errors and not self.warnings:
            print("✅ 검증 통과: 모든 표준을 완벽히 준수합니다!")
        elif not self.errors:
            print(f"⚠️  검증 통과 (경고 {len(self.warnings)}개): 표준을 대체로 준수합니다.")
        else:
            print(f"❌ 검증 실패 (오류 {len(self.errors)}개, 경고 {len(self.warnings)}개)")

        print("="*60 + "\n")

        return len(self.errors) == 0


def main():
    if len(sys.argv) < 2:
        print("사용법: python validate_lithic.py <SVG_파일>")
        print("\n예제:")
        print("  python validate_lithic.py templates/lithic_min.svg")
        print("  python validate_lithic.py my_lithic_drawing.svg")
        sys.exit(1)

    svg_file = sys.argv[1]

    if not Path(svg_file).exists():
        print(f"오류: 파일을 찾을 수 없습니다: {svg_file}")
        sys.exit(1)

    validator = LithicValidator(svg_file)
    success = validator.validate()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

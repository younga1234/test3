---
name: lithic-inkscape-minimal
description: Configure a minimal, standards-compliant Inkscape workspace and template for Paleolithic lithic illustration. Keep only conventions required by accepted lithic standards; remove all non-essential UI, tools, and styles. Output Korean documentation.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash
---

# 구석기 석기 일러스트레이션 Inkscape 최소 템플릿 생성 Skill

## 목표
구석기 석기 실측 도면 전용 Inkscape 환경과 템플릿을 생성·검증합니다. 국제 관례에 필요한 요소만 남기고 나머지를 제거합니다.

**산출물:**
- `templates/lithic_min.svg` - 최소 표준 템플릿
- `styles/line_styles.svg` - 선 스타일 정의
- `symbols/arrows_scalebar.svg` - 기호 라이브러리
- `docs/usage.md` - 사용 가이드 (한국어)
- `docs/checklist.md` - 검증 체크리스트 (한국어)
- `export/pdf_settings.json` - PDF 내보내기 설정

## 입력
- **선택**: `./refs/` 폴더 내 표준·가이드 PDF 요약 메모 (없어도 기본 세트로 진행)
- **선택**: `./refs/sample_lithics/*.jpg` 예시 이미지

## 제약 조건

### 표준 준수 우선
- **방향 체계**: American projection 기본, 이탈 시 도면 내 명시
- **필수 요소**:
  - 외곽선 (outline)
  - 박리흔 경계선 (scar boundaries)
  - 파상선 (ripple marks, 선택)
  - 코르텍스 점묘 (cortex stipple)
  - 세로 단면 (vertical section, 우측 배치)
  - 연결선 (linking lines, 수평)
  - 스케일바 (scale bar)
  - 북화살표 (north arrow)
  - 라벨 (labels)
  - 범례 (legend)

### 시각 스타일 제약
- 흑백 단색 기반, 출판용 선명도 확보
- 선굵기 규격만 허용
- 장식 음영/과도한 방사선·그라디언트 **금지**
- **원칙**: 정보 최대·잉크 최소 (maximum information, minimum ink)

## 절차

### 1) 최소 규격 정의

#### 방향 체계
- American projection 기본
- 예외 시 도면 내 명시

#### 필수 요소 및 선굵기 (mm)
| 요소 | 선굵기 (mm) | 비고 |
|------|-------------|------|
| 외곽선 (outline) | 0.45 | 0.35–0.5 범위 |
| 박리흔 경계선 (scar) | 0.30 | 0.25–0.35 범위 |
| 파상선 (ripple) | 0.20 | 0.18–0.25 범위 |
| 연결선 (linking lines) | 0.15 | 수평, 짧게 |
| 단면 윤곽 (section outline) | 0.45 | 우측 배치 |
| 단면 해칭 (section hatching) | 0.20 | 단면 내부 |
| 코르텍스 점묘 (cortex stipple) | 0.18 | 점 크기 |

#### 라벨 폰트
- 산세리프 (예: Noto Sans CJK KR, Liberation Sans)
- 크기: 7–9 pt
- 일관된 약어 체계 적용

### 2) Inkscape 템플릿 생성 (`templates/lithic_min.svg`)

#### 레이어 구조 (고정)
1. `01_OUTLINE` - 외곽선
2. `02_SCARS` - 박리흔 경계선
3. `03_RIPPLES` - 파상선
4. `04_CORTEX` - 코르텍스 점묘
5. `05_SECTION` - 단면
6. `06_LINKS` - 연결선
7. `07_SYMBOLS` - 기호 (스케일바, 북화살표)
8. `08_LABELS` - 라벨
9. `09_LEGEND` - 범례
10. `10_GUIDES` - 가이드 (비출력)

#### 심볼 라이브러리
- 스케일바: 분절형 1 cm / 5 mm 옵션
- 북화살표: 단순 화살표
- 방향 화살표: 일반 화살표, 헤르츠 콘 원표기 화살표

#### 스타일 시트
- 선 색상: `#000000` (흑색)
- 끝처리: `round`
- 접합: `round`
- 점묘 패턴 정의
- 해칭 패턴 정의 (45도)

#### 페이지 설정
- 크기: A4 (210×297 mm) 또는 A3 (297×420 mm)
- 단위: mm
- 격자: ON, 1 mm 간격
- 스냅: ON
- 기본 배율: 1:1

#### 메타데이터
```xml
<metadata>
  <rdf:RDF>
    <cc:Work>
      <dc:title>구석기 석기 일러스트 최소 표준 템플릿</dc:title>
      <dc:creator>Claude Code - Lithic Inkscape Minimal Skill v1.0.0</dc:creator>
      <dc:description>
        국제 구석기 석기 도면 관례 기반 최소 템플릿.
        American projection 기준.
        출처: Flint Paper Digital, Sidestone Press, Cambridge Stone Tools Guide.
      </dc:description>
      <dc:date>2025</dc:date>
    </cc:Work>
  </rdf:RDF>
</metadata>
```

### 3) 불필요 요소 제거

#### 제거 대상
- 컬러 팔레트 (흑백만 유지)
- 장식용 브러시/필 패턴
- 필터/효과 메뉴 사용법 제외
- 텍스처·그라디언트·블러

#### 경고 주석
템플릿 내 주석으로 다음 추가:
```
⚠ 국제 관례 기반 최소 요소 외 기능과 스타일은 사용하지 말 것
⚠ American projection 기본. 예외는 도면 내 명기
```

### 4) 검증 체크리스트 (`docs/checklist.md`)

다음 항목 포함:
- [ ] American projection 준수 확인
- [ ] 단면 우측 배치 확인
- [ ] 연결선 수평·짧게, 동일 개체 뷰 간 연결
- [ ] 스케일바 실제 길이 검증 (실측 대비)
- [ ] 북화살표 표기
- [ ] 코르텍스 점묘 적용
- [ ] 박리흔 경계선·파상선 구분
- [ ] 선굵기 규격 준수 (outline 0.45, scar 0.30, ripple 0.20 등)
- [ ] 라벨·범례·단위(mm) 일관성
- [ ] PDF 내보내기 시 선 두께 유지
- [ ] 과도한 음영·그라디언트 제거 확인

### 5) 사용 가이드 (`docs/usage.md`)

#### 작업 순서
1. 사진 배치 (가이드 레이어)
2. 외곽선 그리기 (`01_OUTLINE`)
3. 박리흔 경계선 (`02_SCARS`)
4. 파상선 (선택, `03_RIPPLES`)
5. 코르텍스 점묘 (`04_CORTEX`)
6. 단면 그리기 (`05_SECTION`, 우측)
7. 연결선 (`06_LINKS`, 수평)
8. 기호 배치 (`07_SYMBOLS`: 스케일바, 북화살표)
9. 라벨 추가 (`08_LABELS`)
10. 범례 작성 (`09_LEGEND`)
11. 검증 (`docs/checklist.md`)
12. 내보내기 (PDF/SVG)

#### 오류 사례와 수정 팁
- **과도한 음영 제거**: 점묘와 해칭만 사용
- **선굵기 혼용 방지**: 레이어별 스타일 고정
- **비표준 방향 금지**: American projection 엄수
- **연결선 대각선 사용 금지**: 수평선만
- **단면 좌측 배치 금지**: 우측에만 배치

### 6) 내보내기 설정 (`export/pdf_settings.json`)

PDF 내보내기 요구사항:
- PDF/X 또는 벡터 유지 SVG
- 라인 스케일 보존
- 글꼴 임베드
- 래스터화 금지
- 텍스트 윤곽화 옵션

## 출력

### 파일 목록
```
.
├── .claude/
│   └── skills/
│       └── lithic-inkscape/
│           └── SKILL.md
├── templates/
│   └── lithic_min.svg
├── styles/
│   └── line_styles.svg
├── symbols/
│   └── arrows_scalebar.svg
├── docs/
│   ├── usage.md
│   └── checklist.md
├── export/
│   └── pdf_settings.json
└── refs/
    └── sample_lithics/
```

### 요약 보고
- 생성된 파일 목록
- 레이어 구조 확인
- 선굵기 규격 요약
- 사용 가이드 링크

## 오류 처리

- `refs` 폴더 부재 시: 기본 규격으로 진행
- 사용자 스타일 값 있을 경우: 선굵기만 대체
- Inkscape 미설치 경고: 템플릿만 생성, 매뉴얼 사용 안내

## 버전

**v1.0.0** - 최소 규격 릴리스

향후 업데이트 예정:
- 기관별 가이드 매핑 옵션
- GIS 연계 North/Scale 검증 루틴
- 자동 추출 파이프라인 통합

## 참고 문헌

1. Flint Paper Digital - CIfA Guidelines
2. Sidestone Press - Archaeological Illustration Handbook
3. Cambridge - Stone Tools in the Paleolithic and Neolithic Near East
4. Lithics Journal - Standards and Best Practices
5. Peer Community Journal - Lithic Illustration Conventions

---

**주의**: 이 skill은 표준 준수를 최우선으로 합니다. 비표준 요소 사용 시 경고를 발행하며, 출판 및 형상분석 적합성을 보장하기 위해 절차적 일관성을 유지합니다.

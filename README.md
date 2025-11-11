# 구석기 석기 일러스트 Inkscape 최소 템플릿

**버전:** v1.0.0
**날짜:** 2025
**표준:** 국제 구석기 석기 도면 관례 (American Projection)

---

## 개요

구석기 석기 실측 도면을 **국제 관례**에 맞춰 정확하고 일관되게 작성하기 위한 Inkscape 최소 구성 템플릿 및 워크플로우입니다.

### 핵심 원칙

1. **국제 관례 기반 최소 요소만 포함**: American projection, 표준 선굵기, 필수 기호만 사용
2. **정보 최대·잉크 최소**: 필요한 정보만 명확하게 표현하고 불필요한 장식 배제
3. **스케일 정확성**: 실측 크기와 정확히 일치하는 표준화된 도면 작성
4. **출판 품질**: 학술지 제출 및 보존 표준 준수

### 표준 준수

이 템플릿은 다음 국제 표준을 기반으로 합니다:

- Flint Paper Digital (CIfA Guidelines)
- Sidestone Press (Archaeological Illustration Handbook)
- Cambridge - Stone Tools in the Paleolithic and Neolithic Near East
- Lithics Journal - Standards and Best Practices
- Peer Community Journal - Lithic Illustration Conventions

---

## 프로젝트 구조

```
.
├── index.html                              # 🆕 메인 웹 대시보드
├── docs-viewer.html                        # 🆕 문서 뷰어 페이지
├── assets/
│   └── css/
│       └── style.css                       # 🆕 미니멀 UI 스타일 (아이패드 스타일)
├── .claude/
│   └── skills/
│       └── lithic-inkscape/
│           └── SKILL.md                    # Claude Code Skill 정의
├── templates/
│   ├── lithic_min.svg                      # A4 최소 표준 템플릿
│   ├── lithic_min_a3.svg                   # A3 최소 표준 템플릿 (큰 석기용)
│   └── example_lithic.svg                  # 예제 도면
├── styles/
│   └── line_styles.svg                     # 표준 선 스타일 참조
├── symbols/
│   └── arrows_scalebar.svg                 # 심볼 라이브러리 (스케일바, 화살표 등)
├── docs/
│   ├── quick_reference.md                  # 빠른 참조 카드 (1페이지 요약)
│   ├── tutorial.md                         # 단계별 튜토리얼 (초보자용)
│   ├── usage.md                            # 상세 사용 가이드
│   ├── checklist.md                        # 검증 체크리스트
│   └── faq.md                              # 자주 묻는 질문
├── scripts/
│   └── validate_lithic.py                  # 자동 검증 스크립트
├── export/
│   └── pdf_settings.json                   # PDF 내보내기 권장 설정
└── refs/
    └── sample_lithics/                     # 참조 이미지 폴더 (선택)
```

---

## 🌐 웹 인터페이스

브라우저에서 직관적이고 깔끔한 UI로 모든 리소스에 접근하세요:

```bash
# 로컬 서버 실행 (선택사항)
python3 -m http.server 8000

# 브라우저에서 열기
open http://localhost:8000
```

또는 파일을 직접 열기:
- **메인 대시보드**: `index.html` 더블클릭
- **문서 뷰어**: `docs-viewer.html` 더블클릭

### ✨ UI 특징

- **아이패드 스타일 디자인**: 미니멀하고 깔끔한 인터페이스
- **태블릿 펜 최적화**: 큰 터치 영역 (최소 44px), 직관적인 네비게이션
- **반응형 디자인**: 데스크톱, 태블릿, 모바일 모두 지원
- **다크 모드 지원**: 자동 감지 및 적용
- **빠른 접근**: 템플릿, 문서, 도구 한눈에 확인

---

## 빠른 시작

### 1. 템플릿 열기

**웹 인터페이스 사용 (권장)**:
1. `index.html` 파일 더블클릭
2. 원하는 템플릿 카드 클릭

**Inkscape 직접 실행**:
```bash
inkscape templates/lithic_min.svg
```

또는 Inkscape 실행 후: **파일 → 열기** → `templates/lithic_min.svg`

### 2. 새 파일로 저장

템플릿 보존을 위해 새 이름으로 저장:

```
파일 → 다른 이름으로 저장
파일명: 유적명_유물번호_날짜.svg
예: jeonggok_JG2024-001_20250115.svg
```

### 3. 작업 시작

1. 템플릿 안내문 삭제
2. `10_GUIDES` 레이어에 참조 사진 배치
3. 레이어 순서대로 작업 (01_OUTLINE → 02_SCARS → ... → 09_LEGEND)
4. `docs/usage.md` 참조

### 4. 검증 및 내보내기

1. `docs/checklist.md`로 표준 준수 확인
2. **파일 → PDF로 저장**
3. 설정: `export/pdf_settings.json` 참조

---

## 🆕 새로 추가된 기능 (v1.0.0)

### 📖 빠른 참조 카드 (`docs/quick_reference.md`)

1페이지 요약 문서로 가장 자주 사용하는 정보를 빠르게 참조할 수 있습니다:
- 표준 선굵기 일람표
- 레이어 순서 요약
- 필수 규칙 체크리스트
- Inkscape 단축키
- 흔한 오류와 해결책

**언제 사용:** 작업 중 빠른 참조가 필요할 때

### 🎓 단계별 튜토리얼 (`docs/tutorial.md`)

처음 사용하는 분들을 위한 상세한 36단계 가이드:
- 준비부터 완성까지 전 과정
- 스크린샷 대신 명확한 텍스트 설명
- 팁과 요령 포함
- 예상 소요 시간: 30-60분

**언제 사용:** 첫 도면을 작성할 때

### ❓ FAQ (`docs/faq.md`)

32개의 자주 묻는 질문과 답변:
- 일반 질문 (템플릿 용도, 라이선스 등)
- 템플릿 사용법 (시작, A3 템플릿 등)
- 선 스타일 적용 (선굵기, 단위 등)
- 레이어 관리 (순서, 추가 등)
- 심볼 사용 (스케일바, 북화살표 등)
- 내보내기 (PDF, 문제 해결 등)
- 표준 준수 (American Projection, 규칙 등)

**언제 사용:** 문제가 발생했거나 궁금한 점이 있을 때

### ✅ 자동 검증 스크립트 (`scripts/validate_lithic.py`)

SVG 파일의 표준 준수를 자동으로 검증하는 Python 스크립트:

```bash
# 사용법
python3 scripts/validate_lithic.py <SVG_파일>

# 예제
python3 scripts/validate_lithic.py templates/lithic_min.svg
python3 scripts/validate_lithic.py my_drawing.svg
```

**검증 항목:** 페이지 크기, 단위, 레이어 구조, 선 두께, 색상, 메타데이터

**언제 사용:** 작업 완료 후 제출 전 최종 검증

### 📏 A3 템플릿 (`templates/lithic_min_a3.svg`)

큰 석기 작업용 A3 크기 (297mm × 420mm) 템플릿:
- A4 템플릿과 동일한 레이어 구조 및 표준 선굵기
- 더 큰 작업 공간 제공

**언제 사용:** 30cm 이상의 대형 석기 작업 시

---

## 주요 파일 설명

### 📄 `templates/lithic_min.svg`

**Inkscape 최소 표준 템플릿**

- 10개 레이어 구조 (01_OUTLINE ~ 10_GUIDES)
- 표준 선 스타일 정의 (0.45mm, 0.30mm, 0.20mm, 0.15mm)
- 코르텍스 점묘 패턴 (0.18mm)
- 단면 해칭 패턴 (45도)
- A4 페이지, mm 단위, 1mm 격자

**사용법:**
- 이 파일을 복사하여 새 작업 시작
- 레이어 순서대로 작업
- 가이드 레이어(10_GUIDES)는 출력 시 숨김

---

### 📐 `styles/line_styles.svg`

**표준 선 스타일 참조 파일**

7가지 표준 선 스타일 샘플:
1. 외곽선 (0.45mm)
2. 박리흔 경계선 (0.30mm)
3. 파상선 (0.20mm)
4. 연결선 (0.15mm)
5. 단면 윤곽 (0.45mm)
6. 단면 해칭 (0.20mm)
7. 코르텍스 점묘 (0.18mm 점)

**사용법:**
- Inkscape에서 열기
- 원하는 선 스타일 복사
- 작업 도면에 붙여넣기 후 스타일 적용

---

### 🎯 `symbols/arrows_scalebar.svg`

**심볼 라이브러리**

포함된 심볼:
- 스케일바 (1cm, 2cm, 3cm, 5mm)
- 북화살표 (3가지 스타일)
- 방향 화살표 (일반, 헤르츠 콘, 양방향, 곡선)
- 단면 표시 기호

**사용법:**
- 필요한 심볼을 복사하여 `07_SYMBOLS` 레이어에 배치
- 스케일바는 크기 조정 금지 (실제 크기 유지)

---

### 📘 `docs/usage.md`

**상세 사용 가이드 (한국어)**

포함 내용:
- 작업 순서 (단계별 가이드)
- 레이어별 작업 방법
- 선 스타일 적용법
- 심볼 사용법
- 오류 사례와 수정 팁
- 내보내기 방법
- 문제 해결

**대상:** 석기 도면 작성자, 고고학 연구자, 일러스트레이터

---

### ✅ `docs/checklist.md`

**검증 체크리스트 (한국어)**

도면 완성 후 표준 준수 확인:
- 기본 구성 요소 (10개 항목)
- 방향 체계 및 배치 (8개 항목)
- 선 스타일 및 두께 (12개 항목)
- 심볼 및 라벨 (10개 항목)
- 내보내기 설정 (6개 항목)
- 최종 품질 검토 (3개 항목)

**모든 항목 통과 시 출판 및 제출 가능**

---

### ⚙️ `export/pdf_settings.json`

**PDF 내보내기 권장 설정**

포함 내용:
- PDF 버전 권장사항 (PDF/X-1a, PDF/A)
- Inkscape CLI 명령어 예시
- GUI 설정 단계별 안내
- 품질 확인 체크리스트
- 문제 해결 가이드
- 출판 요구사항 (학술지, 출판사, 온라인 저장소)

---

## 표준 선굵기 규격

| 요소 | 선굵기 (mm) | 용도 |
|------|-------------|------|
| **외곽선** | 0.45 | 석기 외곽 윤곽선 |
| **박리흔 경계선** | 0.30 | 격지 제거 흔적 경계 |
| **파상선** | 0.20 | 박리면 파상 무늬 (선택) |
| **연결선** | 0.15 | 뷰 간 수평 연결선 |
| **단면 윤곽** | 0.45 | 단면도 외곽선 |
| **단면 해칭** | 0.20 | 단면 내부 해칭 |
| **코르텍스 점묘** | 0.18 | 점 지름 (자연면) |

**중요:** 이 규격을 벗어나는 선 두께는 사용하지 마세요. 국제 관례 준수가 필수입니다.

---

## Claude Code Skill 사용

이 프로젝트는 Claude Code의 `lithic-inkscape-minimal` skill로 생성되었습니다.

### Skill 실행

```bash
# Claude Code에서 skill 호출
/skill lithic-inkscape
```

또는

```
Skill 도구를 사용하여 "lithic-inkscape" 실행
```

### Skill 위치

`.claude/skills/lithic-inkscape/SKILL.md`

---

## 작업 순서 요약

```
1. 참조 사진 배치 (10_GUIDES)
   ↓
2. 외곽선 (01_OUTLINE, 0.45mm)
   ↓
3. 박리흔 경계선 (02_SCARS, 0.30mm)
   ↓
4. 파상선 (03_RIPPLES, 0.20mm, 선택)
   ↓
5. 코르텍스 점묘 (04_CORTEX, 0.18mm)
   ↓
6. 단면 (05_SECTION, 우측, 0.45mm)
   ↓
7. 연결선 (06_LINKS, 수평, 0.15mm)
   ↓
8. 기호 (07_SYMBOLS: 스케일바, 북화살표)
   ↓
9. 라벨 (08_LABELS, 7-9pt)
   ↓
10. 범례 (09_LEGEND)
   ↓
11. 검증 (docs/checklist.md)
   ↓
12. 내보내기 (PDF/SVG)
```

---

## 필수 확인 사항

### ⚠️ 반드시 지켜야 할 규칙

1. **American Projection 준수** (예외 시 명시)
2. **단면은 항상 우측 배치** (좌측 금지)
3. **연결선은 수평으로만** (대각선 금지)
4. **표준 선굵기 엄수** (외곽 0.45, 박리흔 0.30, 파상선 0.20, 연결선 0.15)
5. **스케일바 크기 정확** (크기 조정 금지)
6. **북화살표 표시** (방향 명확히)
7. **흑백 단색만** (그라디언트·컬러 금지)
8. **최소 잉크 원칙** (과도한 음영 금지)

---

## 출판 및 제출

### 학술지 제출 준비

1. `docs/checklist.md` 모든 항목 확인
2. PDF/X-1a 또는 PDF/A 형식으로 내보내기
3. 해상도 300 DPI 이상 (래스터 요소 포함 시)
4. 메타데이터 포함 (저자, 날짜, 유적명, 유물번호)

### 파일명 규칙

```
유적명_유물번호_날짜.pdf
예: jeonggok_JG2024-001_20250115.pdf
```

### 제출 형식

- **주 형식:** PDF (벡터 유지)
- **보조 형식:** SVG (원본), PNG (미리보기)
- **메타데이터:** 유적명, 유물번호, 작성자, 날짜, 방향 체계

---

## 문의 및 지원

### 문서

- **사용 가이드:** `docs/usage.md`
- **검증 체크리스트:** `docs/checklist.md`
- **PDF 설정:** `export/pdf_settings.json`

### Claude Code Skill

- **Skill 정의:** `.claude/skills/lithic-inkscape/SKILL.md`
- **실행:** `/skill lithic-inkscape`

### 참고 자료

1. [Flint Paper Digital - CIfA Guidelines](https://www.archaeologists.net/sites/default/files/2025-04/flint-paper-digital.pdf)
2. [Sidestone Press - Archaeological Illustration](https://www.sidestone.com/openaccess/9789088905308.pdf)
3. [Cambridge - Stone Tools Guide](https://www.cambridge.org/core/books/stone-tools-in-the-paleolithic-and-neolithic-near-east/lithics-basics/)
4. [Lithics Journal](http://journal.lithics.org/)

---

## 버전 이력

### v1.0.0 (2025)

**최소 규격 릴리스**

- Inkscape 최소 표준 템플릿
- 10개 레이어 구조
- 7가지 표준 선 스타일
- 심볼 라이브러리 (스케일바, 화살표)
- 한국어 사용 가이드 및 체크리스트
- PDF 내보내기 설정
- Claude Code Skill 통합

**향후 업데이트 예정:**
- 기관별 가이드 매핑 옵션
- GIS 연계 North/Scale 검증 루틴
- 자동 추출 파이프라인 통합

---

## 라이선스

이 템플릿과 문서는 **Public Domain - Archaeological Standards Compliant**로 배포됩니다.

학술 및 교육 목적으로 자유롭게 사용, 수정, 배포할 수 있습니다. 단, 국제 고고학 도면 표준 준수를 권장합니다.

---

## 기여

개선 사항, 버그 리포트, 추가 심볼 제안 등은 프로젝트 관리자에게 문의하세요.

---

## 감사의 글

이 프로젝트는 다음 자료를 기반으로 작성되었습니다:

- CIfA (Chartered Institute for Archaeologists) - 석기 도면 디지털 가이드
- Sidestone Press - 고고학 일러스트레이션 핸드북
- Cambridge University Press - 구석기·신석기 석기 도구 가이드
- Lithics Journal - 석기 연구 표준
- Peer Community in Archaeology - 석기 일러스트레이션 관례

---

**⚠ 중요 공지**

> 이 템플릿을 사용하여 작성된 도면은 `docs/checklist.md`의 모든 항목을 통과해야 국제 학술지 출판 및 형상분석에 적합합니다.
>
> **국제 관례 기반 최소 요소 외 기능과 스타일은 사용하지 말 것**
>
> **American projection 기본. 예외는 도면 내 명기**

---

생성: Claude Code - Lithic Inkscape Minimal Skill v1.0.0 (2025)

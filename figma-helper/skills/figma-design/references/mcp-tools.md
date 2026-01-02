# Figma MCP 도구 상세 가이드

## 도구 개요

| 도구명 | 지원 파일 | 용도 |
|--------|-----------|------|
| `get_design_context` | Design, Make | 디자인 컨텍스트 및 코드 생성 |
| `get_metadata` | Design | 레이어 메타데이터 조회 |
| `get_screenshot` | Design, FigJam | 화면 스크린샷 캡처 |
| `get_variable_defs` | Design | 변수 및 스타일 정의 조회 |
| `get_code_connect_map` | Design | 코드 컴포넌트 매핑 조회 |
| `add_code_connect_map` | Design | 코드 컴포넌트 매핑 추가 |
| `create_design_system_rules` | - | 디자인 시스템 규칙 생성 |
| `get_figjam` | FigJam | FigJam 다이어그램 조회 |
| `whoami` | - | 사용자 정보 조회 (원격 전용) |

## 권장 사용 순서

1. **get_design_context** - 항상 먼저 사용하여 전체 컨텍스트 파악
2. **get_metadata** - 필요시 세부 레이어 정보 확인
3. **get_variable_defs** - 디자인 토큰/변수 확인 필요시
4. **get_screenshot** - 레이아웃 정확도 검증 필요시

---

## 1. get_design_context

디자인 요소의 전체 컨텍스트를 조회하고 **코드를 생성**합니다.

### 지원 파일
- Figma Design
- Figma Make

### 기본 동작
- **React + Tailwind CSS** 코드 생성 (기본값)
- 프레임워크 변경 가능 (Vue, HTML+CSS 등)

### 반환 정보
- 요소 구조 (hierarchy)
- 레이아웃 정보 (auto layout, constraints)
- 스타일 정보 (colors, typography, effects)
- 자식 요소 목록
- **생성된 코드** (React/JSX, CSS 등)

### 활용 팁
- 복잡한 컴포넌트 분석 시 필수
- 코드 생성이 필요할 때 이 도구 사용 (별도의 get_code 도구 없음)
- 생성된 코드는 프로젝트 컨벤션에 맞게 수정 필요

---

## 2. get_metadata

특정 Figma 요소의 메타데이터를 조회합니다.

### 지원 파일
- Figma Design

### 반환 형식
- **Sparse XML representation** 형식

### 반환 정보
- 레이어 ID
- 레이어 이름
- 요소 타입 (Frame, Text, Rectangle 등)
- 위치 (position)
- 크기 (dimensions)

### 활용 팁
- 요소 식별이 필요할 때 사용
- 특정 요소 타겟팅 전 확인용
- XML 형식으로 구조 파악 용이

---

## 3. get_screenshot

Figma 화면의 스크린샷을 캡처합니다.

### 지원 파일
- Figma Design
- FigJam

### 반환 정보
- 스크린샷 이미지 데이터
- 캡처 영역 정보

### 활용 팁
- **레이아웃 정확도 유지에 권장**
- 문서화 및 리뷰용으로 활용
- 디자인 변경 이력 기록용
- 코드 구현 결과와 디자인 비교 검증

---

## 4. get_variable_defs

디자인 시스템의 변수와 스타일 정의를 조회합니다.

### 지원 파일
- Figma Design

### 반환 정보
- 색상 변수 (Color tokens)
- 간격 변수 (Spacing tokens)
- 타이포그래피 스타일
- 기타 디자인 토큰

### 활용 팁
- 디자인 시스템 토큰 확인 시 필수
- 변수명과 실제 값 매핑 확인
- 테마 시스템 구현 시 참조

---

## 5. get_code_connect_map

Figma 노드와 코드 컴포넌트 간의 매핑 정보를 조회합니다.

### 지원 파일
- Figma Design

### 반환 정보
- Figma 노드 ID
- 코드 컴포넌트 경로 (`codeConnectSrc`)
- 컴포넌트명 (`codeConnectName`)

### 활용 팁
- 기존 코드 컴포넌트 재사용 확인
- 디자인-코드 연결 상태 파악

---

## 6. add_code_connect_map

Figma 노드와 코드 컴포넌트 간의 매핑을 설정합니다.

### 지원 파일
- Figma Design

### 기능
- Figma 디자인 요소와 실제 코드 컴포넌트 연결
- Code Connect 설정

### 활용 팁
- 컴포넌트 라이브러리 연동 시 사용
- 디자인 시스템과 코드베이스 동기화

---

## 7. create_design_system_rules

디자인 시스템 규칙 파일을 생성합니다.

### 지원 파일
- 파일 컨텍스트 불필요

### 기능
- 에이전트 가이드를 위한 규칙 파일 생성
- 디자인 시스템 일관성 유지

### 활용 팁
- 프로젝트 초기 설정 시 사용
- 팀 협업 규칙 정의

---

## 8. get_figjam

FigJam 다이어그램을 메타데이터로 변환합니다.

### 지원 파일
- FigJam

### 반환 형식
- **XML 형식** 메타데이터

### 활용 팁
- FigJam 다이어그램 분석 시 사용
- 플로우차트, 와이어프레임 등 해석

---

## 9. whoami (원격 전용)

인증된 사용자 정보를 조회합니다.

### 지원 환경
- 원격 MCP 서버 전용

### 반환 정보
- 사용자 이메일
- 플랜 정보
- 좌석 타입 (seat type)

---

## 도구 조합 패턴

### 패턴 1: 전체 컴포넌트 구현
```
get_design_context → 코드 수정 및 최적화
```

### 패턴 2: 디자인 토큰 기반 구현
```
get_variable_defs → get_design_context → 토큰 적용하여 코드 수정
```

### 패턴 3: 디자인 분석
```
get_design_context → get_metadata (세부 요소) → 분석 보고서 작성
```

### 패턴 4: 레이아웃 검증
```
get_screenshot → get_design_context → 구현 후 스크린샷 비교
```

### 패턴 5: 컴포넌트 매핑 확인
```
get_code_connect_map → 기존 컴포넌트 재사용 여부 확인 → get_design_context
```

### 패턴 6: FigJam 다이어그램 분석
```
get_figjam → 구조 분석 → 문서화
```

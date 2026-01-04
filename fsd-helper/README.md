# FSD Helper Plugin

Feature-Sliced Design 아키텍처를 적용한 프론트엔드 프로젝트 개발을 지원하는 Claude Code 플러그인입니다.

## 소개

이 플러그인은 [Feature-Sliced Design](https://feature-sliced.design) 아키텍처 적용 시 필요한 다양한 기능을 제공합니다:

- **구조 생성**: FSD 폴더 구조 초기화 및 슬라이스/세그먼트 생성
- **규칙 검증**: 의존성 규칙 및 구조 검사
- **문서 참조**: 최신 FSD 공식 문서 조회
- **마이그레이션 지원**: 기존 프로젝트를 FSD로 전환하는 가이드

## 사용 방법

### 커맨드

#### `/fsd-init` - 프로젝트 초기화

새 프로젝트에 FSD 폴더 구조를 생성합니다.

```
/fsd-init                    # 기본 React 설정
/fsd-init --framework next   # Next.js 설정
/fsd-init --framework vite   # Vite 설정
```

#### `/fsd-slice` - 슬라이스 생성

레이어에 새 슬라이스를 생성합니다.

```
/fsd-slice entities user
/fsd-slice features auth
/fsd-slice widgets header
/fsd-slice pages home
/fsd-slice features checkout --segments ui,api,model,lib
```

#### `/fsd-segment` - 세그먼트 추가

기존 슬라이스에 세그먼트를 추가합니다.

```
/fsd-segment features/auth api
/fsd-segment entities/user lib
/fsd-segment features/checkout config
```

#### `/fsd-check` - 구조 검증

FSD 규칙 준수 여부를 검사합니다.

```
/fsd-check                   # 전체 검사
/fsd-check --path src/features
/fsd-check --fix             # 수정 제안 포함
```

#### `/fsd-docs` - 문서 조회

FSD 공식 문서를 조회합니다.

```
/fsd-docs                    # 개요
/fsd-docs layers             # 레이어 문서
/fsd-docs rules              # 의존성 규칙
/fsd-docs migration          # 마이그레이션 가이드
/fsd-docs examples           # 예제
```

### 스킬 (자동 활성화)

FSD 관련 질문을 하면 `applying-fsd-architecture` 스킬이 자동으로 활성화됩니다:

```
"FSD에서 features와 entities의 차이가 뭐야?"
"shared 레이어에는 뭘 넣어야 해?"
"features 간에 import가 필요한데 어떻게 해?"
"기존 프로젝트를 FSD로 마이그레이션하려면?"
```

### 에이전트

복잡한 FSD 구조 설계가 필요한 경우 `fsd-architect` 에이전트가 지원합니다:

- 대규모 프로젝트 아키텍처 설계
- 기존 프로젝트 마이그레이션 전략
- 의존성 문제 해결
- 구조 리뷰 및 개선 제안

## FSD 핵심 개념

### 레이어 (Layers)

```
src/
├── app/        # 애플리케이션 진입점
├── pages/      # 라우트 기반 페이지
├── widgets/    # 독립적 UI 블록
├── features/   # 비즈니스 기능
├── entities/   # 비즈니스 엔티티
└── shared/     # 재사용 코드
```

### 의존성 규칙

```
app → pages → widgets → features → entities → shared
```

- 상위 레이어는 하위 레이어만 import 가능
- 같은 레이어 슬라이스 간 import 금지

### 세그먼트 (Segments)

- `ui/` - UI 컴포넌트
- `api/` - API 요청
- `model/` - 비즈니스 로직, 상태
- `lib/` - 유틸리티
- `config/` - 설정

## 플러그인 구조

```
fsd-helper/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── fsd-init.md
│   ├── fsd-slice.md
│   ├── fsd-segment.md
│   ├── fsd-check.md
│   └── fsd-docs.md
├── agents/
│   └── fsd-architect.md
├── skills/
│   └── applying-fsd-architecture/
│       ├── SKILL.md
│       └── references/
│           ├── layers.md
│           ├── slices.md
│           ├── segments.md
│           ├── dependency-rules.md
│           └── migration-guide.md
└── README.md
```

## 라이선스

MIT

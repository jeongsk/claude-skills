# Claude Skills

Claude Code 플러그인 및 스킬 모음입니다.

## 포함된 플러그인

### React Flow Helper

React Flow 라이브러리를 사용한 노드 기반 UI 개발을 지원하는 플러그인입니다.

- 최신 문서 참조 (WebFetch 활용)
- 커스텀 노드/엣지 코드 생성
- 예제 조회 및 프로젝트 설정 가이드

자세한 내용은 [reactflow-helper/README.md](./reactflow-helper/README.md)를 참고하세요.

### FSD Helper

Feature-Sliced Design 아키텍처를 적용한 프론트엔드 프로젝트 개발을 지원하는 플러그인입니다.

- FSD 폴더 구조 초기화 및 슬라이스/세그먼트 생성
- 의존성 규칙 및 구조 검사
- FSD 공식 문서 조회
- 기존 프로젝트 마이그레이션 가이드

자세한 내용은 [fsd-helper/README.md](./fsd-helper/README.md)를 참고하세요.

## 설치 방법

### 방법 1: 명령어로 마켓플레이스 추가

Claude Code에서 다음 명령어를 실행합니다:

```bash
/plugin marketplace add jeongsk/claude-skills
```

마켓플레이스 추가 후 플러그인을 설치합니다:

```bash
# 특정 플러그인 설치
/plugin install reactflow-helper@jeongsk/claude-skills
/plugin install fsd-helper@jeongsk/claude-skills

# 또는 대화형으로 설치
/plugin
```

### 방법 2: 팀 배포

프로젝트에 플러그인 설정을 포함시켜 팀원들이 별도 설치 없이 사용할 수 있습니다.

**설정 방법:**

프로젝트의 `.claude/settings.json` 파일에 다음과 같이 설정합니다:

```json
{
  "enabledPlugins": {
    "reactflow-helper@jeongsk-claude-skills": true,
    "fsd-helper@jeongsk-claude-skills": true
  },
  "extraKnownMarketplaces": {
    "jeongsk-claude-skills": {
      "source": {
        "source": "github",
        "repo": "jeongsk/claude-skills"
      }
    }
  }
}
```

**동작 방식:**

1. 팀원이 저장소를 클론합니다
2. Claude Code가 `.claude/settings.json`을 감지합니다
3. 저장소를 신뢰하면 마켓플레이스와 플러그인이 자동으로 설치됩니다
4. 별도 명령어 없이 바로 플러그인 사용 가능

## 설치 확인

설치 후 다음 명령어로 확인합니다:

```bash
# 마켓플레이스 목록 확인
/plugin marketplace list

# 설치된 플러그인 확인
/plugin
```

## 추천 외부 스킬 및 플러그인

Claude Code 생태계의 유용한 외부 스킬들을 소개합니다.

### 공식 스킬 (Anthropic)

#### example-skills
Anthropic에서 제공하는 공식 예제 스킬 모음입니다.

**주요 기능:**
- **문서 작업**: PDF, DOCX, PPTX, XLSX 파일 생성/편집
- **프론트엔드**: React 컴포넌트, 알고리즘 아트, 캔버스 디자인
- **개발 도구**: MCP 서버 빌더, 웹앱 테스팅, 스킬 생성기
- **커뮤니케이션**: 내부 문서, 테마 팩토리, Slack GIF 생성

**설치:**
```bash
/plugin marketplace add anthropic/example-skills
/plugin install example-skills@anthropic-agent-skills
```

**저장소:** https://github.com/anthropics/anthropic-agent-skills

### 공식 플러그인

#### plugin-dev
Claude Code 플러그인 개발을 위한 종합 도구 모음입니다.

**주요 기능:**
- 플러그인, 명령어, 에이전트, 스킬, 훅 생성 가이드
- MCP 서버 통합 지원
- 플러그인 구조 및 설정 검증

**설치:**
```bash
/plugin marketplace add claude/plugins
/plugin install plugin-dev@claude-plugins-official
```

#### commit-commands
Git 작업을 간소화하는 커밋 관련 명령어 모음입니다.

**주요 기능:**
- `/commit` - 스마트 커밋 생성
- `/commit-push-pr` - 커밋, 푸시, PR 생성 일괄 처리
- `/clean_gone` - 삭제된 원격 브랜치 정리

**설치:**
```bash
/plugin install commit-commands@claude-plugins-official
```

#### feature-dev
복잡한 기능 개발을 위한 가이드형 개발 도구입니다.

**주요 기능:**
- 코드베이스 이해 및 아키텍처 분석
- 단계별 기능 개발 가이드
- 기존 패턴 준수

**설치:**
```bash
/plugin install feature-dev@claude-plugins-official
```

#### pr-review-toolkit
포괄적인 Pull Request 리뷰 도구 모음입니다.

**주요 기능:**
- 코드 품질, 스타일, 보안 검사
- 에러 처리 및 테스트 커버리지 분석
- 타입 설계 및 코드 복잡도 리뷰

**설치:**
```bash
/plugin install pr-review-toolkit@claude-plugins-official
```

## 사용 방법

### React Flow Helper 커맨드

| 커맨드                   | 설명                      |
| ------------------------ | ------------------------- |
| `/rf-docs [주제]`        | React Flow 공식 문서 조회 |
| `/rf-node [이름]`        | 커스텀 노드 컴포넌트 생성 |
| `/rf-edge [이름]`        | 커스텀 엣지 컴포넌트 생성 |
| `/rf-example [카테고리]` | 예제 코드 조회            |
| `/rf-setup`              | 프로젝트 초기 설정 가이드 |

### 예시

```bash
# API 문서 조회
/rf-docs api

# 커스텀 노드 생성
/rf-node DatabaseNode --resizable

# 레이아웃 예제 조회
/rf-example layout dagre

# 프로젝트 설정
/rf-setup --typescript --tailwind
```

## 새 플러그인 추가하기

새 플러그인을 추가하려면:

1. 플러그인 디렉토리 생성
2. `.claude-plugin/plugin.json` 작성
3. 루트의 마켓플레이스에 플러그인 등록
4. `settings.json`에 활성화 추가

자세한 플러그인 개발 가이드는 [Claude Code 플러그인 문서](https://code.claude.com/docs/plugins)를 참고하세요.

## 라이선스

MIT

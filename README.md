# Claude Skills

Claude Code 플러그인 및 스킬 모음입니다.

## 포함된 플러그인

### React Flow Helper

React Flow 라이브러리를 사용한 노드 기반 UI 개발을 지원하는 플러그인입니다.

- 최신 문서 참조 (WebFetch 활용)
- 커스텀 노드/엣지 코드 생성
- 예제 조회 및 프로젝트 설정 가이드

자세한 내용은 [reactflow-helper/README.md](./reactflow-helper/README.md)를 참고하세요.

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
    "reactflow-helper@jeongsk-claude-skills": true
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

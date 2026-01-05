# Claude Skills

Claude Code 플러그인 및 스킬 모음입니다.

## 포함된 플러그인

### 기능 플러그인

#### React Flow Helper

React Flow 라이브러리를 사용한 노드 기반 UI 개발을 지원하는 플러그인입니다.

- 최신 문서 참조 (WebFetch 활용)
- 커스텀 노드/엣지 코드 생성
- 예제 조회 및 프로젝트 설정 가이드

자세한 내용은 [reactflow-helper/README.md](./reactflow-helper/README.md)를 참고하세요.

#### FSD Helper

Feature-Sliced Design 아키텍처를 적용한 프론트엔드 프로젝트 개발을 지원하는 플러그인입니다.

- FSD 폴더 구조 초기화 및 슬라이스/세그먼트 생성
- 의존성 규칙 및 구조 검사
- FSD 공식 문서 조회
- 기존 프로젝트 마이그레이션 가이드

자세한 내용은 [fsd-helper/README.md](./fsd-helper/README.md)를 참고하세요.

#### Git Workflow

Git 워크플로우 자동화 플러그인입니다.

- 논리적 단위별 커밋 생성
- 커밋 & 푸시 자동화
- PR 생성까지 원스톱 처리

자세한 내용은 [git-workflow/README.md](./git-workflow/README.md)를 참고하세요.

#### Figma Helper

Figma Dev Mode MCP를 활용한 디자인-코드 변환 지원 플러그인입니다.

- Figma 디자인에서 코드 추출
- 컴포넌트 구조 분석
- 스타일 코드 생성

자세한 내용은 [figma-helper/README.md](./figma-helper/README.md)를 참고하세요.

#### Skill Finder

유용한 외부 Claude Code 스킬과 플러그인을 찾아주는 대화형 도우미입니다.

- 로컬 데이터베이스 검색
- SkillsMP API 실시간 검색
- 카테고리별 필터링

자세한 내용은 [skill-finder/README.md](./skill-finder/README.md)를 참고하세요.

### 출력 스타일 플러그인

#### Output Styles

Claude의 응답 스타일을 커스터마이징하는 플러그인입니다.

- **Korean**: 모든 응답을 한국어로 제공
- **Concise**: 짧고 핵심만 전달하는 간결한 스타일

자세한 내용은 [output-styles/README.md](./output-styles/README.md)를 참고하세요.

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


## 새 플러그인 추가하기

새 플러그인을 추가하려면:

1. 플러그인 디렉토리 생성
2. `.claude-plugin/plugin.json` 작성
3. 루트의 마켓플레이스에 플러그인 등록
4. `settings.json`에 활성화 추가

자세한 플러그인 개발 가이드는 [Claude Code 플러그인 문서](https://code.claude.com/docs/plugins)를 참고하세요.

## 추천 외부 스킬 및 플러그인

유용한 외부 스킬과 플러그인은 [추천 플러그인 문서](./docs/recommended-plugins.md)를 참고하세요.

## References

- Agent Skills 개요: https://platform.claude.com/docs/ko/agents-and-tools/agent-skills/overview
- Agent Skills 시작하기: https://platform.claude.com/docs/ko/agents-and-tools/agent-skills/quickstart
- Skill 작성 모범 사례: https://platform.claude.com/docs/ko/agents-and-tools/agent-skills/best-practices
- Claude Code 플러그인 개요: https://code.claude.com/docs/ko/plugins
- Claude Code 플러그인 참조: https://code.claude.com/docs/ko/plugins-reference
- 프롬프트 엔지니어링 개요: https://platform.claude.com/docs/ko/build-with-claude/prompt-engineering/overview
- 프롬프트 작성 모범 사례: https://platform.claude.com/docs/ko/build-with-claude/prompt-engineering/claude-4-best-practices

## 라이선스

[MIT License](./LICENSE)

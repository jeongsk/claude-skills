# Skill Finder

유용한 외부 Claude Code 스킬과 플러그인을 찾아주는 대화형 도우미입니다.

## 개요

Claude Code 생태계에는 많은 유용한 스킬과 플러그인이 존재합니다. Skill Finder는 사용자가 원하는 기능이나 목적에 맞는 스킬을 쉽게 찾을 수 있도록 도와줍니다.

## 특징

- **대화형 검색**: 자연어로 원하는 기능을 설명하면 적합한 스킬 추천
- **포괄적 데이터베이스**: 공식 스킬 및 커뮤니티 스킬 정보 제공
- **상세한 정보**: 각 스킬의 기능, 설치 방법, 사용 사례 안내
- **키워드 검색**: PDF, Git, React 등 키워드로 빠른 검색

## 설치

### 마켓플레이스에서 설치

```bash
/plugin marketplace add jeongsk/claude-skills
/plugin install skill-finder@jeongsk-claude-skills
```

### 팀 배포 (프로젝트 설정)

프로젝트의 `.claude/settings.json`에 추가:

```json
{
  "enabledPlugins": {
    "skill-finder@jeongsk-claude-skills": true
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

## 사용 방법

### 스킬 검색

자연어로 원하는 기능을 설명하세요:

```
"PDF 작업할 수 있는 스킬 있어?"
"Git 커밋을 도와주는 플러그인 찾아줘"
"코드 리뷰 자동화 도구 추천해줘"
"프론트엔드 개발에 유용한 스킬은?"
```

### 명령어

```bash
/find-skills [키워드 또는 설명]
```

## 지원하는 스킬 카테고리

### 공식 스킬 (Anthropic)
- **example-skills**: PDF, DOCX, PPTX, XLSX 문서 작업, React 컴포넌트, MCP 빌더 등

### 공식 플러그인
- **plugin-dev**: 플러그인 개발 도구
- **commit-commands**: Git 커밋 자동화
- **feature-dev**: 기능 개발 가이드
- **pr-review-toolkit**: PR 리뷰 자동화
- **code-review**: 코드 리뷰

### 커뮤니티 리소스
- GitHub의 claude-code 토픽
- 커뮤니티 큐레이션 목록

## 예시

### 예시 1: PDF 관련 스킬 찾기

**입력:**
```
PDF 파일 작업할 수 있는 스킬 있어?
```

**출력:**
```
## 추천 스킬: example-skills

**설명**: Anthropic에서 제공하는 공식 예제 스킬 모음입니다.
**제공자**: Anthropic (공식)

### 주요 기능

**문서 작업**
- PDF 파일 생성/편집/분석
- DOCX 문서 생성/편집
- PPTX 프레젠테이션 생성/편집
- XLSX 스프레드시트 생성/편집

### 설치 방법

\`\`\`bash
/plugin marketplace add anthropic/example-skills
/plugin install example-skills@anthropic-agent-skills
\`\`\`

### 이런 경우에 유용합니다

- 문서 자동화가 필요한 프로젝트
- 프론트엔드 컴포넌트 빠른 프로토타이핑
- MCP 서버 개발
```

### 예시 2: Git 도구 찾기

**입력:**
```
Git 커밋 자동화 도구 추천해줘
```

**출력:**
```
Git 커밋 관련해서 두 가지 좋은 옵션이 있습니다:

## 1. commit-commands (공식 플러그인)

**주요 기능:**
- `/commit` - 스마트 커밋 메시지 생성
- `/commit-push-pr` - 커밋, 푸시, PR 생성 일괄 처리

## 2. git-workflow (이 저장소의 플러그인)

**주요 기능:**
- 변경 사항을 논리적 단위로 자동 그룹화
- 의미 있는 커밋 메시지 자동 생성
```

## 데이터베이스

스킬 정보는 [`external-skills-database.json`](../external-skills-database.json)에 저장됩니다.

### 데이터베이스 구조

```json
{
  "version": "1.0.0",
  "lastUpdated": "2026-01-04",
  "categories": {
    "official-skills": { ... },
    "official-plugins": { ... },
    "community-resources": { ... }
  },
  "searchIndex": {
    "keywords": { ... }
  }
}
```

### 새 스킬 추가

새로운 스킬을 데이터베이스에 추가하려면:

1. `external-skills-database.json` 파일 편집
2. 적절한 카테고리에 스킬 정보 추가
3. `searchIndex`에 키워드 등록
4. Pull Request 생성

## 고급 기능

### 키워드 검색

데이터베이스의 `searchIndex` 섹션을 활용한 빠른 키워드 매칭:

- PDF, Excel, DOCX 등 파일 형식
- Git, React, MCP 등 기술 키워드
- 개발, 리뷰, 테스트 등 작업 유형

### 다중 스킬 추천

하나의 질문에 여러 관련 스킬을 함께 추천하여 사용자가 최적의 선택을 할 수 있도록 지원합니다.

### 사용 사례 기반 추천

각 스킬의 `useCases` 정보를 활용하여 사용자의 상황에 맞는 스킬을 추천합니다.

## 제한사항

- 데이터베이스는 수동으로 큐레이션됨 (정기 업데이트 필요)
- 모든 커뮤니티 스킬을 포함하지 않음
- 스킬 버전 정보는 실시간으로 업데이트되지 않음

## 로드맵

- [ ] 자동 데이터베이스 업데이트
- [ ] GitHub API 연동으로 최신 정보 가져오기
- [ ] 사용자 평점 및 리뷰 시스템
- [ ] 스킬 카테고리 자동 분류

## 기여하기

새로운 스킬 추가나 개선 제안은 환영합니다!

1. 이슈 생성 또는 PR 제출
2. `external-skills-database.json` 업데이트
3. 스킬 정보 검증

## 라이선스

MIT

## 관련 링크

- [메인 저장소](https://github.com/jeongsk/claude-skills)
- [Claude Code 공식 문서](https://code.claude.com)
- [Claude Code GitHub Topic](https://github.com/topics/claude-code)

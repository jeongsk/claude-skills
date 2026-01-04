# Skill Finder

유용한 외부 Claude Code 스킬과 플러그인을 찾아주는 대화형 도우미입니다.

## 개요

Claude Code 생태계에는 많은 유용한 스킬과 플러그인이 존재합니다. Skill Finder는 사용자가 원하는 기능이나 목적에 맞는 스킬을 쉽게 찾을 수 있도록 도와줍니다.

## 특징

- **대화형 검색**: 자연어로 원하는 기능을 설명하면 적합한 스킬 추천
- **2단계 검색 시스템**:
  - 로컬 큐레이션 데이터베이스 (공식 스킬 우선)
  - SkillsMP API 실시간 검색 (커뮤니티 스킬)
- **포괄적 정보**: 공식 스킬부터 최신 커뮤니티 스킬까지
- **인기도 기반 추천**: SkillsMP stars 수를 기반으로 검증된 스킬 우선 제공
- **상세한 정보**: 각 스킬의 기능, 설치 방법, 사용 사례, 저장소 링크
- **키워드 검색**: PDF, Git, React 등 키워드로 빠른 검색 (한글/영어 모두 지원)

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

## 검색 소스

### 1. 로컬 큐레이션 데이터베이스
검증된 공식 스킬과 플러그인 정보를 담은 로컬 데이터베이스:

**공식 스킬 (Anthropic)**
- **example-skills**: PDF, DOCX, PPTX, XLSX 문서 작업, React 컴포넌트, MCP 빌더 등

**공식 플러그인**
- **plugin-dev**: 플러그인 개발 도구
- **commit-commands**: Git 커밋 자동화
- **feature-dev**: 기능 개발 가이드
- **pr-review-toolkit**: PR 리뷰 자동화
- **code-review**: 코드 리뷰

### 2. SkillsMP API (실시간)
커뮤니티가 공유하는 최신 스킬을 실시간으로 검색:

- **실시간 검색**: 최신 커뮤니티 스킬 발견
- **인기도 정렬**: stars 수 기준으로 검증된 스킬 우선 제공
- **다양한 카테고리**: 개발, 문서, AI, 유틸리티 등
- **직접 방문**: https://skillsmp.com

### 검색 전략

1. **로컬 우선**: 큐레이션된 공식 스킬을 먼저 검색
2. **API 보완**: 로컬 DB에 없으면 SkillsMP에서 검색
3. **병합 결과**: 두 소스의 결과를 합쳐 최적의 추천 제공
4. **중복 제거**: 같은 스킬이 양쪽에 있으면 하나만 표시

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

### 예시 3: SkillsMP에서 검색

**입력:**
```
이미지 처리 스킬 찾아줘
```

**검색 과정:**
1. 로컬 데이터베이스에서 "image" 키워드 검색 → 결과 없음
2. SkillsMP API로 "image processing" 검색
3. 인기도(stars) 순으로 정렬된 결과 제공

**출력:**
```
"image processing"으로 SkillsMP에서 검색한 결과입니다:

## 1. image-optimizer

**설명**: AI-powered image optimization and conversion tool
**제공자**: john-dev (커뮤니티)
**인기도**: ⭐ 245
**마켓플레이스**: image-tools-marketplace

### 주요 기능
- 이미지 자동 최적화 및 압축
- 다양한 포맷 변환 (PNG, JPG, WebP, AVIF)
- AI 기반 이미지 품질 향상

### 설치 방법
\`\`\`bash
/plugin marketplace add john-dev/image-tools
/plugin install image-optimizer@image-tools-marketplace
\`\`\`

더 많은 결과: https://skillsmp.com/search?q=image%20processing
```

## 데이터 소스

### 로컬 데이터베이스

스킬 정보는 [`external-skills-database.json`](skills/external-skills-database.json)에 저장됩니다.

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

새로운 스킬을 로컬 데이터베이스에 추가하려면:

1. `skills/external-skills-database.json` 파일 편집
2. 적절한 카테고리에 스킬 정보 추가
3. `searchIndex`에 키워드 등록
4. Pull Request 생성

### SkillsMP 검색 스크립트

실시간 커뮤니티 스킬 검색을 위한 Python 스크립트:

**스크립트 위치**: `scripts/search_skills.py`

**사용 방법**:
```bash
python3 scripts/search_skills.py "[검색어]" --limit 5
```

**옵션**:
| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `--limit N` | 반환할 결과 수 | 10 |
| `--page N` | 페이지 번호 | 1 |
| `--sort` | 정렬 기준 (stars/recent/name) | stars |
| `--format` | 출력 형식 (json/text) | json |

**예시**:
```bash
# PDF 관련 스킬 검색
python3 scripts/search_skills.py "pdf" --limit 5

# Git 스킬을 최신순으로 검색
python3 scripts/search_skills.py "git" --sort recent --limit 3
```

**응답 형식**:
```json
{
  "success": true,
  "query": "pdf",
  "total": 479,
  "skills": [
    {
      "name": "pdf",
      "author": "anthropics",
      "description": "PDF manipulation toolkit...",
      "stars": 24530,
      "githubUrl": "https://github.com/...",
      "hasMarketplace": true
    }
  ]
}
```

**장점**:
- WebFetch 대비 토큰 사용량 대폭 감소
- 필요한 정보만 간결하게 반환
- 최신 커뮤니티 스킬 실시간 발견
- 인기도 검증 (stars 기준)

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
2. `skills/external-skills-database.json` 업데이트
3. 스킬 정보 검증

## 라이선스

MIT

## 관련 링크

- [메인 저장소](https://github.com/jeongsk/claude-skills)
- [Claude Code 공식 문서](https://code.claude.com)
- [Claude Code GitHub Topic](https://github.com/topics/claude-code)

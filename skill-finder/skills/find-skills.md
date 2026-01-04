---
title: 외부 스킬 찾기
description: 목적에 맞는 외부 Claude Code 스킬과 플러그인을 찾아드립니다
---

# 외부 스킬 찾기

사용자가 원하는 기능이나 목적에 맞는 Claude Code 스킬 및 플러그인을 추천하는 대화형 도우미입니다.

## Resources

이 스킬은 다음 리소스를 참조합니다:

- **외부 스킬 데이터베이스**: `${CLAUDE_PLUGIN_ROOT}/../external-skills-database.json` - 공식 및 커뮤니티 스킬 정보
- **README**: `${CLAUDE_PLUGIN_ROOT}/../README.md` - 추가 정보 및 설치 가이드

## Instructions

### 1. 사용자 의도 파악

사용자가 다음과 같은 요청을 할 때 이 스킬이 활성화됩니다:
- "PDF 작업할 수 있는 스킬 있어?"
- "Git 커밋을 도와주는 플러그인 찾아줘"
- "코드 리뷰 자동화 도구 추천해줘"
- "프론트엔드 개발에 유용한 스킬은?"
- 기타 기능이나 목적 기반 스킬 검색 요청

### 2. 검색 및 분석 프로세스

1. **키워드 추출**: 사용자 요청에서 핵심 키워드 추출
   - 예: "PDF", "Git", "코드 리뷰", "React" 등

2. **데이터베이스 조회**: `external-skills-database.json` 파일 읽기
   - 키워드를 사용해 `searchIndex` 섹션에서 관련 스킬 찾기
   - 카테고리별로 스킬 정보 탐색

3. **매칭 및 필터링**:
   - 사용자 요청과 가장 관련성 높은 스킬 1-3개 선별
   - 각 스킬의 features, useCases 확인

### 3. 응답 형식

사용자에게 다음 정보를 제공합니다:

#### 기본 정보
```
## 추천 스킬: [스킬 이름]

**설명**: [스킬 설명]
**제공자**: [공식/커뮤니티]
**태그**: [관련 태그들]
```

#### 주요 기능
스킬의 주요 기능을 카테고리별로 나열:
```
### 주요 기능

**[카테고리 1]**
- 기능 1
- 기능 2

**[카테고리 2]**
- 기능 3
- 기능 4
```

#### 설치 방법
```
### 설치 방법

\`\`\`bash
[설치 명령어들]
\`\`\`

[추가 설명이 있다면 포함]
```

#### 사용 사례
```
### 이런 경우에 유용합니다

- 사용 사례 1
- 사용 사례 2
- 사용 사례 3
```

#### 추가 정보
```
### 더 알아보기

- **저장소**: [GitHub URL]
- **관련 문서**: [문서 링크]
```

### 4. 다중 스킬 추천

여러 스킬이 관련될 경우:
1. 가장 적합한 스킬을 먼저 소개
2. 관련된 다른 스킬들도 간략히 언급
3. 사용자가 선택할 수 있도록 옵션 제시

### 5. 검색 결과 없음

관련 스킬을 찾지 못한 경우:
```
죄송합니다. "[검색어]"와 관련된 스킬을 데이터베이스에서 찾을 수 없습니다.

다음을 시도해보세요:
- 다른 키워드로 검색
- Claude Code 마켓플레이스 확인: `/plugin marketplace list`
- GitHub에서 "claude-code" 토픽 검색: https://github.com/topics/claude-code
```

## 예시

### 예시 1: PDF 관련 스킬 검색

**사용자**: "PDF 파일 작업할 수 있는 스킬 있어?"

**응답**:
```
## 추천 스킬: example-skills

**설명**: Anthropic에서 제공하는 공식 예제 스킬 모음입니다.
**제공자**: Anthropic (공식)
**태그**: official, documents, frontend, development-tools

### 주요 기능

**문서 작업**
- PDF 파일 생성/편집/분석
- DOCX 문서 생성/편집
- PPTX 프레젠테이션 생성/편집
- XLSX 스프레드시트 생성/편집

**프론트엔드**
- React 컴포넌트 디자인
- 알고리즘 아트 생성 (p5.js)
- 캔버스 디자인
- 웹 아티팩트 빌더

**개발 도구**
- MCP 서버 빌더
- 웹앱 테스팅 (Playwright)
- 스킬 생성기

### 설치 방법

\`\`\`bash
/plugin marketplace add anthropic/example-skills
/plugin install example-skills@anthropic-agent-skills
\`\`\`

설치 후 개별 스킬을 바로 사용할 수 있습니다.

### 이런 경우에 유용합니다

- 문서 자동화가 필요한 프로젝트
- 프론트엔드 컴포넌트 빠른 프로토타이핑
- MCP 서버 개발
- 비주얼 콘텐츠 생성

### 더 알아보기

- **저장소**: https://github.com/anthropics/anthropic-agent-skills
```

### 예시 2: Git 관련 스킬 검색

**사용자**: "Git 커밋 자동화 도구 추천해줘"

**응답**:
```
Git 커밋 관련해서 두 가지 좋은 옵션이 있습니다:

## 1. commit-commands (공식 플러그인)

**설명**: Git 작업을 간소화하는 커밋 관련 명령어 모음
**제공자**: Claude Code Official

### 주요 기능
- `/commit` - 스마트 커밋 메시지 생성
- `/commit-push-pr` - 커밋, 푸시, PR 생성 일괄 처리
- `/clean_gone` - 삭제된 원격 브랜치 정리

### 설치 방법
\`\`\`bash
/plugin install commit-commands@claude-plugins-official
\`\`\`

---

## 2. git-workflow (이 저장소의 플러그인)

**설명**: 변경 사항을 논리적 단위로 자동 분석하여 커밋
**제공자**: jeongsk

### 주요 기능
- 변경 사항을 논리적 단위로 자동 그룹화
- 의미 있는 커밋 메시지 자동 생성
- 단계별 커밋 또는 일괄 커밋 & 푸시

### 설치 방법
\`\`\`bash
/plugin marketplace add jeongsk/claude-skills
/plugin install git-workflow@jeongsk-claude-skills
\`\`\`

어떤 스킬이 더 필요하신지 알려주시면 자세한 사용법을 안내해드리겠습니다!
```

## 참고사항

- 데이터베이스는 정기적으로 업데이트됩니다 (`lastUpdated` 필드 확인)
- 새로운 스킬 추가 요청은 저장소 이슈로 제출 가능
- 공식 스킬은 Anthropic 및 Claude Code Official에서 관리
- 커뮤니티 스킬은 개별 개발자가 관리

## 추가 기능

### 카테고리별 탐색

사용자가 "전체 스킬 목록 보여줘" 또는 "카테고리별로 보여줘" 요청 시:
1. 데이터베이스의 `categories` 섹션 읽기
2. 각 카테고리별로 스킬 요약 제공
3. 사용자가 관심 있는 카테고리 선택 가능

### 태그 기반 검색

사용자가 특정 태그로 검색 요청 시:
- `official`, `development`, `git`, `documents` 등의 태그로 필터링
- 해당 태그를 가진 모든 스킬 나열

## 오류 처리

- 파일을 읽을 수 없는 경우: 사용자에게 README 참조 안내
- JSON 파싱 오류: 관리자에게 문제 보고 요청
- 빈 검색 결과: 대체 검색 방법 제안

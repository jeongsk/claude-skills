# 추천 외부 스킬 및 플러그인

Claude Code 생태계의 유용한 외부 스킬들을 소개합니다.

## 공식 스킬 (Anthropic)

### example-skills
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

## 공식 플러그인

### plugin-dev
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

### commit-commands
Git 작업을 간소화하는 커밋 관련 명령어 모음입니다.

**주요 기능:**
- `/commit` - 스마트 커밋 생성
- `/commit-push-pr` - 커밋, 푸시, PR 생성 일괄 처리
- `/clean_gone` - 삭제된 원격 브랜치 정리

**설치:**
```bash
/plugin install commit-commands@claude-plugins-official
```

### feature-dev
복잡한 기능 개발을 위한 가이드형 개발 도구입니다.

**주요 기능:**
- 코드베이스 이해 및 아키텍처 분석
- 단계별 기능 개발 가이드
- 기존 패턴 준수

**설치:**
```bash
/plugin install feature-dev@claude-plugins-official
```

### pr-review-toolkit
포괄적인 Pull Request 리뷰 도구 모음입니다.

**주요 기능:**
- 코드 품질, 스타일, 보안 검사
- 에러 처리 및 테스트 커버리지 분석
- 타입 설계 및 코드 복잡도 리뷰

**설치:**
```bash
/plugin install pr-review-toolkit@claude-plugins-official
```

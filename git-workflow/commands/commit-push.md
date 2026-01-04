---
description: "현재까지의 작업을 논리적 단위별로 나눠서 commit & push"
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git log:*), Bash(git diff:*), Bash(git push:*), Bash(git branch:*)
model: haiku
---

# 작업 단위별 commit & push 명령어

## Role

Git 커밋 전문가로서, 변경사항을 분석하고 의미 있는 단위로 분리하여 Conventional Commits 형식의 커밋을 생성한 후 원격 저장소에 반영합니다.

## Purpose

코드 변경사항을 논리적 단위로 분리하여 각각 독립적이고 의미 있는 커밋으로 만들고, 원격 저장소에 push하여 팀과 공유합니다.

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## 변경사항 그룹화 기준

다음 기준으로 관련 변경사항을 그룹화합니다:

1. **기능 단위**: 하나의 기능을 완성하는 파일들
2. **레이어 단위**: 같은 레이어(UI, 로직, 데이터)의 변경
3. **의존성**: 서로 의존하는 변경들은 함께 커밋
4. **독립성**: 독립적으로 리버트 가능해야 함

### 분리해야 하는 경우

- 기능 추가 + 버그 수정 → 별도 커밋
- 리팩토링 + 새 기능 → 별도 커밋
- 포맷팅 + 로직 변경 → 별도 커밋

## 수행 단계

### 1. 작업을 논리적 단위로 분류

Context의 변경사항을 분석하여 관련된 것끼리 그룹화합니다:

- 관련된 변경사항끼리 묶어서 분류
- 각 그룹이 하나의 완성된 기능/수정 단위가 되도록 구성

### 2. 각 단위별로 순차 commit

가장 핵심적인 변경부터 시작하여 각 작업 단위별로 commit을 생성합니다:

1. 해당 작업 단위의 파일들을 스테이징
   ```bash
   git add [관련 파일들]
   ```

2. 컨벤션에 맞는 commit 메시지 작성
   - 형식: `type(scope): 설명`
   - 타입 종류:
     - `feat`: 새로운 기능 추가
     - `fix`: 버그 수정
     - `refactor`: 코드 리팩토링
     - `docs`: 문서 수정
     - `style`: 코드 포맷팅, 세미콜론 누락 등
     - `test`: 테스트 코드 추가/수정
     - `chore`: 빌드 설정, 패키지 매니저 등
   - 설명은 현재형으로 작성 (예: "add" not "added")
   - 제목은 50자 이내로 작성

3. commit 실행
   ```bash
   git commit -m "type(scope): 설명"
   ```

### 3. commit 완료 확인

모든 commit이 완료된 후 결과를 확인합니다:
- `git log --oneline -10`으로 생성된 commit 이력 확인
- `git status`로 남은 변경사항 확인

### 4. 원격 저장소에 push

commit된 변경사항을 원격 저장소에 반영합니다:

1. 기본 push 실행
   ```bash
   git push origin <current-branch>
   ```

2. push 실패 시 대응
   - **업스트림 미설정**: 새 브랜치인 경우 upstream 설정과 함께 push
     ```bash
     git push -u origin <branch-name>
     ```
   - **충돌 발생**: 원격 브랜치의 변경사항을 먼저 pull하여 병합
   - **권한 문제**: 저장소 접근 권한 확인 필요함을 안내

3. push 결과 확인

## Examples

### 입력 상황

```
modified: src/auth/login.ts (로그인 버그 수정)
modified: src/auth/types.ts (타입 수정)
modified: src/users/profile.ts (새 기능 추가)
modified: README.md (문서 업데이트)
```

### 기대 출력

```bash
# Commit 1: 버그 수정
git add src/auth/login.ts src/auth/types.ts
git commit -m "fix(auth): resolve login validation error"

# Commit 2: 새 기능
git add src/users/profile.ts
git commit -m "feat(users): add profile avatar upload"

# Commit 3: 문서
git add README.md
git commit -m "docs: update installation guide"

# Push
git push origin feature/user-improvements
```

## Constraints

<critical>
- 민감한 파일(.env, credentials.json 등)은 절대 커밋하지 않음
- 커밋 없이 메시지만 출력하지 않음 - 반드시 실제 커밋 수행
- 변경사항이 없으면 커밋하지 않음
- force push는 절대 사용하지 않음
</critical>

<important>
- 각 커밋은 독립적으로 리버트 가능해야 함
- 관련 없는 변경사항은 반드시 별도 커밋으로 분리
- 커밋 메시지는 50자 이내로 작성
- 하나의 커밋은 하나의 논리적 변경만 포함
- push 전 원격 브랜치와의 충돌 여부 확인
</important>

## Arguments

`$ARGUMENTS` 처리:
- **제공됨**: 해당 메시지를 단일 커밋 메시지로 사용 (모든 변경사항을 하나의 커밋으로)
- **미제공**: 변경사항을 분석하여 논리적 단위별로 자동 분리 커밋

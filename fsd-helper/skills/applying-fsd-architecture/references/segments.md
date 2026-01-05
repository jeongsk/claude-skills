# FSD Segments Reference

## 세그먼트 개요

세그먼트는 슬라이스 내부에서 코드를 기술적 역할별로 분류하는 단위입니다.

## 표준 세그먼트

### 1. ui/

UI 컴포넌트와 관련 스타일을 포함합니다.

```
features/auth/ui/
├── LoginForm.tsx
├── LoginForm.module.css
├── LoginForm.test.tsx
├── LogoutButton.tsx
└── index.ts
```

```typescript
// ui/LoginForm.tsx
import styles from './LoginForm.module.css';
import { Button, Input } from '@/shared/ui';

export function LoginForm({ onSubmit }: LoginFormProps) {
  return (
    <form className={styles.form} onSubmit={onSubmit}>
      <Input name="email" type="email" />
      <Input name="password" type="password" />
      <Button type="submit">로그인</Button>
    </form>
  );
}
```

### 2. api/

외부 API와의 통신을 담당합니다.

```
features/auth/api/
├── login.ts
├── logout.ts
├── refreshToken.ts
├── types.ts
└── index.ts
```

```typescript
// api/login.ts
import { apiClient } from '@/shared/api';
import type { LoginRequest, LoginResponse } from './types';

export async function login(data: LoginRequest): Promise<LoginResponse> {
  return apiClient.post('/auth/login', data);
}
```

### 3. model/

비즈니스 로직, 상태 관리, 타입 정의를 포함합니다.

```
features/auth/model/
├── types.ts           # 타입 정의
├── authStore.ts       # 상태 관리 (Zustand/Redux)
├── useAuth.ts         # 커스텀 훅
├── selectors.ts       # 셀렉터
└── index.ts
```

```typescript
// model/authStore.ts
import { create } from 'zustand';
import type { AuthState } from './types';

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  setUser: (user) => set({ user, isAuthenticated: !!user }),
  logout: () => set({ user: null, isAuthenticated: false }),
}));
```

```typescript
// model/types.ts
export interface User {
  id: string;
  email: string;
  name: string;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  setUser: (user: User | null) => void;
  logout: () => void;
}
```

### 4. lib/

슬라이스 내에서 사용되는 유틸리티 함수입니다.

```
features/auth/lib/
├── validateEmail.ts
├── validatePassword.ts
├── formatAuthError.ts
└── index.ts
```

```typescript
// lib/validatePassword.ts
export function validatePassword(password: string): string | null {
  if (password.length < 8) {
    return '비밀번호는 8자 이상이어야 합니다';
  }
  if (!/[A-Z]/.test(password)) {
    return '대문자를 포함해야 합니다';
  }
  return null;
}
```

### 5. config/

슬라이스별 설정값과 상수를 정의합니다.

```
features/auth/config/
├── constants.ts
├── authConfig.ts
└── index.ts
```

```typescript
// config/constants.ts
export const AUTH_CONFIG = {
  TOKEN_KEY: 'auth_token',
  REFRESH_TOKEN_KEY: 'refresh_token',
  SESSION_TIMEOUT: 30 * 60 * 1000, // 30분
} as const;
```

## 세그먼트 구조 패턴

### 최소 구조

작은 기능의 경우:

```
features/toggle-theme/
├── ui/
│   └── ThemeToggle.tsx
├── model/
│   └── useTheme.ts
└── index.ts
```

### 표준 구조

일반적인 기능의 경우:

```
features/auth/
├── ui/
├── api/
├── model/
└── index.ts
```

### 완전한 구조

복잡한 기능의 경우:

```
features/checkout/
├── ui/
├── api/
├── model/
├── lib/
├── config/
└── index.ts
```

## 세그먼트별 Export 규칙

각 세그먼트는 자체 `index.ts`를 가지며, 슬라이스의 `index.ts`에서 re-export합니다:

```typescript
// features/auth/ui/index.ts
export { LoginForm } from './LoginForm';
export { LogoutButton } from './LogoutButton';

// features/auth/model/index.ts
export { useAuthStore } from './authStore';
export type { User, AuthState } from './types';

// features/auth/index.ts (Public API)
export { LoginForm, LogoutButton } from './ui';
export { useAuthStore } from './model';
export type { User, AuthState } from './model';
```

## Shared 레이어의 세그먼트

Shared 레이어는 슬라이스 없이 세그먼트만 사용합니다:

```
shared/
├── ui/                # UI 컴포넌트 키트
│   ├── Button/
│   ├── Input/
│   ├── Modal/
│   └── index.ts
├── api/               # API 클라이언트
│   ├── client.ts
│   └── index.ts
├── lib/               # 유틸리티
│   ├── cn.ts
│   ├── formatDate.ts
│   └── index.ts
├── config/            # 전역 설정
│   └── constants.ts
└── types/             # 공통 타입
    └── common.ts
```

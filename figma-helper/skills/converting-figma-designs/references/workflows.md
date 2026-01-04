# Figma MCP 워크플로우 예시

## 워크플로우 1: 디자인 시스템 컴포넌트 구현

### 시나리오
디자인 시스템의 버튼 컴포넌트를 React로 구현

### 단계

1. **디자인 컨텍스트 파악**
   ```
   → get_design_context 호출
   → 버튼의 variants, states, 스타일 정보 확인
   ```

2. **코드 생성**
   ```
   → get_code 호출
   → 기본 JSX/CSS 코드 획득
   ```

3. **코드 최적화**
   - TypeScript 타입 추가
   - variant props 정의
   - 스타일을 프로젝트 컨벤션에 맞게 수정
   - 접근성 속성 추가

### 결과물 예시
```tsx
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'ghost';
  size: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
}

export const Button = ({ variant, size, children, onClick }: ButtonProps) => {
  return (
    <button
      className={cn(buttonVariants({ variant, size }))}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

## 워크플로우 2: 페이지 레이아웃 구현

### 시나리오
대시보드 페이지 레이아웃을 구현

### 단계

1. **전체 구조 분석**
   ```
   → get_design_context 호출
   → 레이아웃 구조 (header, sidebar, main) 파악
   → Auto Layout 설정 확인
   ```

2. **섹션별 메타데이터 확인**
   ```
   → get_metadata 호출 (각 주요 섹션)
   → 컴포넌트 분리 계획 수립
   ```

3. **코드 생성 및 조합**
   ```
   → get_code 호출 (각 섹션)
   → 컴포넌트 분리
   → 레이아웃 조합
   ```

### 베스트 프랙티스
- Grid/Flexbox 레이아웃으로 변환
- 반응형 브레이크포인트 추가
- 컴포넌트 경계 명확히 분리

## 워크플로우 3: 아이콘 시스템 구축

### 시나리오
디자인의 아이콘들을 SVG로 추출하여 아이콘 시스템 구축

### 단계

1. **아이콘 요소 파악**
   ```
   → get_metadata 호출
   → 아이콘 요소들의 이름과 구조 확인
   ```

2. **SVG 추출**
   ```
   → get_image 호출 (각 아이콘)
   → SVG 형식으로 내보내기
   ```

3. **아이콘 컴포넌트 생성**
   - SVG를 React 컴포넌트로 변환
   - size, color props 추가
   - 아이콘 인덱스 파일 생성

### 결과물 구조
```
icons/
├── index.ts
├── IconSearch.tsx
├── IconHome.tsx
├── IconSettings.tsx
└── ...
```

## 워크플로우 4: 디자인 QA 및 문서화

### 시나리오
디자인 구현 결과를 검증하고 문서화

### 단계

1. **디자인 스크린샷 캡처**
   ```
   → get_screenshot 호출
   → 원본 디자인 이미지 저장
   ```

2. **디자인 스펙 추출**
   ```
   → get_design_context 호출
   → 색상, 타이포그래피, 스페이싱 정보 추출
   ```

3. **문서 생성**
   - 디자인 스펙 문서 작성
   - 스크린샷 첨부
   - 구현 노트 추가

## 워크플로우 5: 반응형 디자인 구현

### 시나리오
데스크톱/모바일 디자인을 반응형으로 구현

### 단계

1. **각 브레이크포인트 분석**
   ```
   → get_design_context 호출 (데스크톱)
   → get_design_context 호출 (모바일)
   → 차이점 파악
   ```

2. **공통 요소 추출**
   ```
   → get_code 호출
   → 공통 스타일과 구조 식별
   ```

3. **반응형 스타일 적용**
   - 미디어 쿼리 추가
   - 유동적 레이아웃 적용
   - 터치 인터랙션 고려

### 팁
- 모바일 퍼스트 접근 권장
- CSS 변수로 브레이크포인트 관리
- 컨테이너 쿼리 활용 고려

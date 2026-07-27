# 📝 프롬프트 스튜디오 (Prompt Studio)
> **파이썬 콘솔 기반 프롬프트 관리 시스템**

AI 프롬프트를 카테고리별로 효율적으로 관리, 검색 및 즐겨찾기(⭐)할 수 있는 CLI 프롬프트 관리 프로그램입니다.

## 1. 프로젝트 개요
- **프로젝트명**: 프롬프트 스튜디오 (Prompt Studio)
- **개발 언어**: Python 3.10+
- **주요 목적**: 파이썬 콘솔 기반 프롬프트 관리 및 Git 원자적 커밋(Atomic Commit) 실습

## 2. 주요 기능 및 함수 명세
- **📱 메뉴 & 프레임워크**
  - `show_menu()`: 메인 메뉴 화면 출력
  - `main()`: 메인 프로그램 실행 및 입력 루프
- **✏️ 프롬프트 관리**
  - `add_prompt()`: 신규 프롬프트 추가 및 입력값 검증
  - `show_list()`: 전체 프롬프트 목록 출력 및 ⭐ 표시
  - `show_detail()`: 프롬프트 상세 보기
- **🔍 검색 및 필터링**
  - `filter_by_category()`: 카테고리별 프롬프트 조회
  - `search_prompt()`: 키워드 검색
- **⭐ 즐겨찾기 관리**
  - `toggle_favorite()`: 즐겨찾기 등록 및 해제
  - `show_favorites()`: 즐겨찾기 목록 모아보기

## 3. 개발 및 커밋 로드맵
- **[Commit 1]** `feat`: 저장소 초기 설정
- **[Commit 2]** `feat`: .gitignore 제외 파일 추가
- **[Commit 3]** `docs`: README.md 프로젝트 개요 및 구조 작성 (프롬프트 스튜디오)
- *(이하 순차적 구현 예정)*

## 4. 디렉토리 구조
```text
prompt_manager/
├── main.py            # 메인 실행 코드 및 기능 함수
├── README.md          # 프로젝트 설명 문서
├── .gitignore         # Git 추적 제외 파일
└── proof_shots/       # 실습 스크린샷 및 제출용 첨부 자료
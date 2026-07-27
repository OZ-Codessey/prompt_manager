# ⚜️ PROMPT ...Manager

> ###  *Orange Boîte* 브랜드 헤리티지와 파이썬 CLI가 결합된 프롬프트 관리 시스템    
>>-프롬프트를 효율적으로 관리할 수 있는 CLI 프롬프트 관리 프로그램입니다.


<br> 

##  Overview
| 항목 | 상세 내용 |
| :--- | :--- | 
| **프로젝트명** | *PARANSÊ PROMPT STUDIO* | 
| **개발 환경** | Python 3.12+ / macOS CLI (Zsh) | 
| **디자인 콘셉트** |  *Orange Boîte Theme* (ANSI Color Palette) | 
| **핵심 목적** | AI 프롬프트 체계적 관리 및 기능 단위 커밋 실습 |
---  
<br>

## How to Run

>터미널(Terminal) 환경에서 아래 명령어를 입력하여 프로그램을 실행합니다.

```sh
python3 main.py  
```  

<br>  

##  Prompt Categories Guide
>본 스튜디오에 수록된 프롬프트는 아래 6가지 핵심 카테고리로 체계적으로 분류되어 관리됩니다.
1. 🎨 이미지 생성 (Image Generation)
    * 미드저니(Midjourney) 등 AI 이미지 생성 모델에 최적화된 하이엔드 로고 및 비주얼 생성 프롬프트
2. 🎬 영상 생성 (Video Generation)
    * 엔드 프레임 연동, 시네마틱 라이팅, 카메라 워킹이 지정된 브랜드 로고 영상 연출 프롬프트
3. 🎵 오디오 생성 (Audio Generation)
    * Suno AI 등 BGM/오케스트라 생성에 활용되는 웅장한 시네마틱 음악 생성 프롬프트
4. 🎭 페르소나 (Persona & Worldview)
    * 브랜드의 인문학적 서사, 세계관, 1:1 맞춤 메시징 톤앤매너 설정 지시문
5. ⚙️ 자동화 (Automation & Template)
    * 고객 문의 수신 시 자동으로 발송되는 이메일 템플릿 및 텍스트 명함 결합 지시문
6. 📂 기타 (Heritage & Philosophy)
    * 브랜드 헤리티지 컬러 가이드(Orange Boîte) 및 주거 철학 재해석 텍스트  

<br>  

## Core Features & Function Reference
*  메인 프레임워크 & 메뉴
    * show_menu(): Orange Boîte 컬러 파렛트가 적용된 메인 메뉴 UI 출력
    * main(): 키보드 입력 루프 제어 및 메뉴 대화형 실행
*  전체 컬렉션 조회 & 상세 보기
    * show_list(): 전체 프롬프트 목록 포맷팅 출력 및 즐겨찾기([★ FAVORITE]) 태그 표시
    * open_detail_view() / show_single_detail(): ID 선택을 통한 제목·카테고리·본문 상세 조회
* 🔍 스마트 키워드 검색
    * search_prompt(): 제목, 카테고리, 본문 통합 부분 문자열 검색 및 하이라이팅 표시
*  카테고리별 동적 필터링
    * show_by_category(): 정해진 사용자 정의 정렬 순서(이미지~기타)에 따른 카테고리 분류 조회
* ★ 셀렉션 즐겨찾기 관리
    * show_favorites(): 즐겨찾기 등록 프롬프트만 모아보기
    * toggle_favorite(): 특정 프롬프트의 즐겨찾기 상태 On/Off 스위칭
<br><br>

## Git Commit Log

| 커밋 단계 | 커밋 메시지 (Commit Message) | 주요 작업 내용 |
| :--- | :--- | :--- |
| **Commit 1** | `first commit` | 저장소 초기화 및 기본 파일 생성 |
| **Commit 2** | `제외 파일 추가` | `.gitignore` 추적 제외 파일 설정 |
| **Commit 3** | `style: Initialize Orange Boite design system and prompt dataset` | 디자인 시스템 ANSI 컬러 및 초기 01~08 프롬프트 데이터 구축 |
| **Commit 4** | `feat: Add main menu UI and full collection list feature` | 메인 메뉴 UI 및 전체 프롬프트 컬렉션 조회 기능 구현 |
| **Commit 5** | `feat: Add prompt detail view functionality` | 프롬프트 ID 선택 및 상세 내용 보기 화면 구현 |
| **Commit 6** | `feat: Implement smart search with partial matching and highlighting` | 키워드 동적 검색 및 검색어 하이라이팅 기능 구현 |
| **Commit 7** | `feat: Add dynamic category filtering functionality` | 카테고리 동적 필터링 및 조회 기능 구현 |
| **Commit 8** | `refactor: Apply custom sorting order to category filter menu` | 카테고리 정렬 순서 개선 ('기타' 항목을 맨 뒤로 이동) |
| **Commit 9** | `feat: Add selection favorites toggle feature and finalize main application` | 셀렉션 즐겨찾기 관리/토글 스위치 구현 및 메인 앱 완성 |
| **Commit 10** | `docs: Update README with project guidelines and real commit history` | 교안 요구사항 충족 프로젝트 문서 작성 및 커밋 로그 정리 |  
<br><br>


###  Directory Structure 
```
prompt_manager/
├── main.py            # 프롬프트 스튜디오 메인 실행 프로그램
├── README.md          # 프로젝트 안내 및 교안 요건 작성 문서
├── .gitignore         # macOS / Python Git 추적 제외 설정 파일
└── records/           # 실습 스크린샷 및 제출용 첨부 자료 폴더
```
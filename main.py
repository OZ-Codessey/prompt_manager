import os
import re
import sys

# ==============================================================================
# 1. 브랜드 디자인 시스템 (Orange Boîte Heritage Color Palette)
# ==============================================================================
PARANSE_ORANGE = "\033[38;2;243;112;33m\033[1m"       # Header Accent: Primary Bold Orange (#F37021)
ORANGE_BG_TEXT = "\033[48;2;243;112;33m\033[38;2;20;18;15m\033[1m" # Search Highlight
HEADER_WHITE   = "\033[38;2;245;240;235m\033[1m"     # Header Sub Accent: Bold Ivory (#F5F0EB)
MENU_TEXT      = "\033[38;2;215;210;205m\033[22m"    # Menu Item Text: Regular Slim Soft Cream
CREAM_WHITE    = "\033[38;2;245;240;235m"            # Main Text: Soft Ivory
WARM_TAUPE     = "\033[38;2;160;140;125m"            # Divider: Warm Taupe (#A08C7D)
DEEP_SADDLE    = "\033[38;2;200;160;120m"            # Sub Accent: Saddle Tan (#C8A078)
MUTED_GRAY     = "\033[38;2;100;90;85m"              # Exit/System Sub Label: Muted Gray
RESET          = "\033[0m"                           # Color Reset

LINE_DIVIDER   = f"{WARM_TAUPE}────────────────────────────────────────────────────{RESET}"

# ==============================================================================
# 2. 초기 프롬프트 데이터셋 (01번 ~ 08번 원본 100% 수록)
# ==============================================================================
prompts = [
    {
        "id": 1,
        "title": "무지개 너머 여정을 떠나는 파란새",
        "category": "이미지 생성",
        "content": """나무 창틀 집 안쪽에 앉아 열린 창문 너머 비 개인 언덕과 아름다운 무지개를 바라보는 파란새, 창가에는 화분이 놓여 있고 평범하고 따뜻한 가정 분위기, 시네마틱 라이팅. 미드저니로 생성한 최고급 창호와 스테인드글라스 배경 이미지 중앙에, 우아하고 클래식한 세리프(Serif) 계열 폰트로 브랜드 이름 'Parang-Sê'를 정교하게 합성. 철자는 P와 S만 대문자여야 하며(Parang-Sê), 소문자 'r'의 오른쪽 곡선 위에는 아주 작은 파란새 한 마리가 사뿐히 내려앉고, 소문자 'e' 위의 악상시르콤플렉스는 지붕 모양으로 변환 형상화. 텍스트 전체는 고품질의 프리미엄 골드톤과 브러시드 금속 질감을 살려 극도의 럭셔리함을 나타내어 배경과 로고가 하이엔드 무드로 완벽히 어우러진 깨끗한 최종 로고 이미지 생성""",
        "is_favorite": True,
    },
    {
        "id": 2,
        "title": "엔드 프레임 연동 브랜드 로고 영상",
        "category": "영상 생성",
        "content": """The video must end exactly with the attached image as the final frame. A premium brand video maintaining strict visual consistency. The scene is set on a premium, high-performance, high-tech dark system window sill with a sophisticated wood-like finish, with vivid raindrops realistically splashing on it, against a background of a stained glass window illuminated by warm golden sunset light. On the left side of the sill, a larger bluebird sits quietly but subtly moves its wings on the spot. In the center, the elegant brushed-gold serif text 'Parang-Sê' shimmers with a glittering light effect sweeping from left to right. Inside this scene, an extremely tiny, hyper-cute baby bluebird energetically flaps its wings as it flies from the upper left sky (11 o'clock direction) and lands gently on the alphabet letter 'r' in elegant slow motion. Simultaneously, a small roof-shaped symbol spins down energetically from the upper right sky (2 o'clock direction) and settles smoothly on top of the letter 'e' in slow motion, perfectly culminating in the exact composition of the final frame. High detail, seamless cinematic animation.""",
        "is_favorite": True,
    },
    {
        "id": 3,
        "title": "영웅적 서사의 웅장한 시네마틱 오케스트라",
        "category": "오디오 생성",
        "content": "",
        "is_favorite": False,
    },
    {
        "id": 4,
        "title": "Parang-Sê 브랜드 페르소나",
        "category": "페르소나",
        "content": """당신은 모리스 마테르링크의 희곡 《파랑새(L'Oiseau bleu)》를 모티브로 한 프리미엄 Sur Mesure 하우징 브랜드 'Parang-Sê'의 메신저입니다.

[브랜드 본질 & 서사]
• 인문학적 모티브: 긴 여정 끝에 자신의 집에서 진짜 파란새를 발견하듯, 세상의 소음과 시련을 막아주고 절대적 안식을 제공하는 '내 집'의 본질적 가치를 공간화합니다.
• Sur Mesure 독점성: 규격화된 기성 창호를 배제하고, 건축주의 취향에 맞춰 1:1 맞춤 제작되는 최고급 컬러 유리 및 시스템 창호를 지향합니다.
• 핵심 메시지: 세상의 소음과 혹독한 악천후마저 오직 나만을 위한 단 하나의 풍경으로 치환하여 흔들리지 않는 내면의 평온(Inner Peace)을 선사하세요.""",
        "is_favorite": True,
    },
    {
        "id": 5,
        "title": "고객 문의 접수 및 자동 답장 서비스",
        "category": "자동화",
        "content": """[자동화 업무 지시문]
contact@paranse.com으로 고객 문의가 접수되면, 아래 양식의 자동 답장 메일과 Sur-Mesure 텍스트 명함을 결합하여 즉시 발송하세요.

[자동 발송 메일 템플릿]
보내주신 문의가 정상적으로 접수되었습니다.

"세상의 소음과 악천후를 풍경으로 바꾸는 단 하나의 프레임"

┌──────────────────────────────────────────────────────────┐
│ PARANG-SÊ | SUR-MESURE COULEUR & FRAME                   │
│ Contact : contact@paranse.com                            │
└──────────────────────────────────────────────────────────┘""",
        "is_favorite": False,
    },
    {
        "id": 6,
        "title": "Parang-Sê & Orange Boîte 브랜드 헤리티지 컬러 가이드",
        "category": "기타",
        "content": """[Parang-Sê Heritage Color Palette]
• Primary Accent    : Orange Boîte (Pantone 165 C / Hex: #F37021 / RGB: 243, 112, 33)
• Secondary Leather : Saddle Tan (Hex: #C8A078 / RGB: 200, 160, 120)
• Structural Neutral: Warm Taupe (Hex: #A08C7D / RGB: 160, 140, 125)
• Text Contrast     : Cream Ivory (Hex: #F5F0EB / RGB: 245, 240, 235)
• Design Concept    : 오랑주 보아트(Orange Boîte)의 하이엔드 럭셔리 감성과 프롬프트 매니저 화면의 가독성을 완벽하게 결합한 시각 디자인 시스템""",
        "is_favorite": True,
    },
    {
        "id": 7,
        "title": "",
        "category": "오디오 생성",
        "content": """sunoAI prompt: Cinematic orchestral, modern neoclassical, storytelling background music, emotional, dynamic progression, 30-second commercial arc, 85 BPM. Instrumentation: melancholic solo piano, dramatic cinematic strings, ambient brass, warm acoustic guitar, evolving synthesizer pads.""",
        "is_favorite": False,
    },
    {
        "id": 8,
        "title": "브랜드철학_《파랑새(L'Oiseau bleu)》의 재해석",
        "category": "",
        "content": """주인공 남매가 행복을 찾아 고난의 여정을 헤매다 결국 자신의 집(Home)에서 파랑새를 발견하듯, 인간이 누릴 수 있는 최상의 안식과 완전한 보호는 가장 사적인 공간인 '내 집' 안에 존재한다는 본질적 진리를 주거 미학으로 복원합니다.

Parang-Sê는 '파랑새'의 인문학적 성찰을 사적인 주거 공간의 미학으로 완벽히 투영합니다. 일상의 긴 여정 끝에 비로소 당도하는 나만의 성역. 그 안에서 세상의 모든 소요(騷擾)를 거르고 온전한 안식과 평온을 소유하게 하는 것, 그것이 프리미엄 하우징 브랜드 Parang-Sê가 선사하는 본질적 가치입니다.""",
        "is_favorite": True,
    },
]

# ==============================================================================
# 3. 유틸리티 함수
# ==============================================================================
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_clean_input(prompt_text):
    try:
        return input(prompt_text).strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  프로그램을 종료합니다.")
        sys.exit(0)

def highlight_text(text, keyword):
    if not keyword or not text:
        return text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return pattern.sub(lambda m: f"{ORANGE_BG_TEXT}{m.group(0)}{RESET}{CREAM_WHITE}", text)

# ==============================================================================
# 4. 주요 화면 및 기능 구현
# ==============================================================================
def show_menu():
    clear_screen()
    print("\n" + LINE_DIVIDER)
    print(f"             {PARANSE_ORANGE}P A R A N S Ê   B U S A N{RESET}             ")
    print(f"                 {HEADER_WHITE}P R O M P T   S T U D I O{RESET}         ")
    print(LINE_DIVIDER)
    print(f"   {MENU_TEXT}1. 전체 컬렉션 조회{RESET}            {MUTED_GRAY}(Collection List){RESET}")
    print(f"   {MENU_TEXT}2. 프롬프트 상세 보기{RESET}          {MUTED_GRAY}(Prompt Detail){RESET}")
    print(f"   {MENU_TEXT}3. 스마트 키워드 검색{RESET}          {MUTED_GRAY}(Smart Search){RESET}")
    print(f"   {MENU_TEXT}4. 카테고리별 조회{RESET}            {MUTED_GRAY}(Filter by Category){RESET}")
    print(f"   {MUTED_GRAY}Q. 스튜디오 종료               (Exit Studio){RESET}")
    print(LINE_DIVIDER)

def show_list(prompts_list, title_text="ALL PROMPT COLLECTION"):
    clear_screen()
    print("\n" + LINE_DIVIDER)
    print(f"   {PARANSE_ORANGE}+ {title_text}{RESET}")
    print(LINE_DIVIDER + "\n")

    if not prompts_list:
        print(f"   ⚠️ {MUTED_GRAY}등록되거나 조건에 맞는 프롬프트가 없습니다.{RESET}\n")
    else:
        for p in prompts_list:
            fav_tag = f"[{PARANSE_ORANGE}★ FAVORITE{RESET}]" if p["is_favorite"] else f"[{MUTED_GRAY} Standard {RESET}]"
            p_id = f"{p['id']:02d}"
            t_text = p["title"].strip() if p["title"].strip() else "(제목 없음)"
            c_text = f"({p['category'].strip()})" if p["category"].strip() else "(카테고리 미지정)"
            print(f"   {p_id}  {fav_tag} {t_text} {c_text}")

    print("\n" + LINE_DIVIDER)

def open_detail_view(prompts_list):
    show_list(prompts_list, "PROMPT DETAIL VIEW")
    choice = get_clean_input(f"   {PARANSE_ORANGE}👉 프롬프트 ID 선택 [1~{len(prompts_list)}, b: 메인 메뉴] : {RESET}")
    
    if choice.lower() in ['b', 'back']:
        return

    if not choice.isdigit():
        get_clean_input(f"   👉 {MUTED_GRAY}올바른 숫자 번호를 입력해 주세요. (Enter: 메인 메뉴){RESET}")
        return

    target_id = int(choice)
    target = next((p for p in prompts_list if p["id"] == target_id), None)

    if not target:
        get_clean_input(f"   👉 {MUTED_GRAY}해당 ID의 프롬프트를 찾을 수 없습니다. (Enter: 메인 메뉴){RESET}")
        return

    show_single_detail(target)

def show_single_detail(target, keyword=""):
    clear_screen()
    fav_status = f"{PARANSE_ORANGE}★ FAVORITE{RESET}" if target["is_favorite"] else f"{MUTED_GRAY}Standard{RESET}"
    
    title_display = target["title"].strip() if target["title"].strip() else "(제목 없음)"
    cat_display = target["category"].strip() if target["category"].strip() else "(카테고리 미지정)"
    content_display = target["content"].strip() if target["content"].strip() else f"{MUTED_GRAY}(내용 없음 / 비어있음){RESET}"

    if keyword:
        title_display = highlight_text(title_display, keyword)
        cat_display = highlight_text(cat_display, keyword)
        if target["content"].strip():
            content_display = highlight_text(content_display, keyword)

    print("\n" + LINE_DIVIDER)
    print(f"   {PARANSE_ORANGE}📄 PROMPT DETAIL VIEW [{target['id']:02d}]{RESET}")
    print(LINE_DIVIDER)
    print(f"   {CREAM_WHITE}• 제목       :{RESET} {title_display}")
    print(f"   {CREAM_WHITE}• 카테고리   :{RESET} {cat_display}")
    print(f"   {CREAM_WHITE}• 즐겨찾기   :{RESET} {fav_status}")
    print(LINE_DIVIDER)
    print(f"   {WARM_TAUPE}[ 프롬프트 내용 (Content) ]{RESET}\n")
    print(f"   {content_display}")
    print("\n" + LINE_DIVIDER)
    
    get_clean_input(f"   👉 {MUTED_GRAY}Enter 키를 누르면 메인 메뉴로 돌아갑니다...{RESET}")

def search_prompt(prompts_list):
    clear_screen()
    print("\n" + LINE_DIVIDER)
    print(f"   {PARANSE_ORANGE}🔍 SMART KEYWORD SEARCH{RESET}")
    print(LINE_DIVIDER + "\n")

    keyword = get_clean_input(f"   {PARANSE_ORANGE}👉 검색 키워드 입력 [b: 메인 메뉴] : {RESET}")
    if keyword.lower() in ['b', 'back'] or not keyword:
        return

    results = [
        p for p in prompts_list 
        if keyword.lower() in p["title"].lower() 
        or keyword.lower() in p["content"].lower() 
        or keyword.lower() in p["category"].lower()
    ]

    clear_screen()
    print("\n" + LINE_DIVIDER)
    print(f"   {PARANSE_ORANGE}+ SEARCH RESULTS FOR '{keyword}'{RESET}")
    print(LINE_DIVIDER + "\n")

    if not results:
        print(f"   ⚠️ {MUTED_GRAY}'{keyword}'에 일치하는 프롬프트가 없습니다.{RESET}\n")
    else:
        for p in results:
            fav_tag = f"[{PARANSE_ORANGE}★ FAVORITE{RESET}]" if p["is_favorite"] else f"[{MUTED_GRAY} Standard {RESET}]"
            p_id = f"{p['id']:02d}"
            
            t_raw = p["title"].strip() if p["title"].strip() else "(제목 없음)"
            c_raw = p["category"].strip() if p["category"].strip() else "카테고리 미지정"
            
            t_hl = highlight_text(t_raw, keyword)
            c_hl = highlight_text(c_raw, keyword)
            
            print(f"   {p_id}  {fav_tag} {t_hl} ({c_hl})")

    print("\n" + LINE_DIVIDER)
    choice = get_clean_input(f"   {PARANSE_ORANGE}👉 프롬프트 ID 선택 [b: 메인 메뉴] : {RESET}")
    if choice.isdigit():
        target_id = int(choice)
        target = next((p for p in results if p["id"] == target_id), None)
        if target:
            show_single_detail(target, keyword)

def show_by_category(prompts_list):
    clear_screen()
    print("\n" + LINE_DIVIDER)
    print(f"   {PARANSE_ORANGE}📁 FILTER BY CATEGORY{RESET}")
    print(LINE_DIVIDER + "\n")

    category_order = ["이미지 생성", "영상 생성", "오디오 생성", "페르소나", "자동화", "기타"]
    extracted = list(set(p["category"].strip() for p in prompts_list if p["category"].strip()))
    
    categories = sorted(
        extracted, 
        key=lambda c: category_order.index(c) if c in category_order else 999
    )

    for idx, cat in enumerate(categories, 1):
        print(f"     {idx}. {cat}")
    
    choice = get_clean_input(f"\n   {PARANSE_ORANGE}👉 Category 선택 [1~{len(categories)}, b: 메인 메뉴] : {RESET}")
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected_cat = categories[int(choice) - 1]
        filtered = [p for p in prompts_list if p["category"] == selected_cat]
        show_list(filtered, f"CATEGORY: {selected_cat}")
        get_clean_input(f"   👉 {MUTED_GRAY}Enter 키를 누르면 메인 메뉴로 돌아갑니다...{RESET}")

def main():
    while True:
        show_menu()
        choice = get_clean_input(f"   {PARANSE_ORANGE}👉 Select Menu [1~4, Q] : {RESET}")

        if choice == '1':
            show_list(prompts, "ALL PROMPT COLLECTION")
            get_clean_input(f"   👉 {MUTED_GRAY}Enter 키를 누르면 메인 메뉴로 돌아갑니다...{RESET}")
        elif choice == '2':
            open_detail_view(prompts)
        elif choice == '3':
            search_prompt(prompts)
        elif choice == '4':
            show_by_category(prompts)
        elif choice.lower() in ['q', 'exit', 'quit']:
            clear_screen()
            print("\n" + LINE_DIVIDER)
            print(f"   {PARANSE_ORANGE}⚜️  PARANG-SÊ BUSAN PROMPT STUDIO를 이용해 주셔서 감사합니다.{RESET}")
            print(f"   {WARM_TAUPE}“L'art de la parole et de la pensée.”{RESET}")
            print(LINE_DIVIDER + "\n")
            break
        else:
            get_clean_input(f"   ⚠️ {MUTED_GRAY}잘못된 입력입니다. [1~4, Q] 중 선택해 주세요.{RESET}")

if __name__ == "__main__":
    main()
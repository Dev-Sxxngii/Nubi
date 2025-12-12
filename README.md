아래는 Nubi 프로젝트를 기준으로 작성한 GitHub `README.md` 예시입니다.
현재 업로드된 코드 구조(PyQt5 GUI, Selenium 기반 크롤링, Excel 저장, 의존성 주입 구조 등)를 반영하여 비교적 완성도 있게 작성하였습니다.
바로 사용하시거나, 원하시는 방향에 맞게 세부 문구만 조정하셔도 됩니다.

---

# Nubi

Nubi는 이커머스 상품 검색 결과를 손쉽게 수집하고 엑셀로 정리할 수 있는 데스크톱 크롤링 도구입니다.
GUI 환경에서 검색어, 조건, 페이지 수만 입력하면 Selenium 기반 크롤러가 자동으로 데이터를 수집하고, 결과를 Excel 파일로 저장할 수 있도록 설계되었습니다.

본 프로젝트는 크롤링 로직과 UI를 명확히 분리하고, 의존성 주입(Dependency Injection) 구조를 적용하여 확장성과 유지보수성을 고려해 개발되었습니다.

---

## 주요 기능

* PyQt5 기반 GUI 제공
* 이커머스 사이트 상품 검색 크롤링
* 검색 조건 선택 기능

  * 추천순
  * 판매순
  * 최신순
* 수집 페이지 수 설정
* Excel(.xlsx) 파일 자동 생성 및 저장
* 크롤링 성공/실패에 따른 UI 상태 피드백
* 사이트별 환경 설정 분리 지원

---

## 지원 사이트

* NAVER
* COUPANG
* 11번가(ELEVEN)

※ 사이트별 크롤링 로직은 환경 변수 및 컨트롤러 구조를 통해 독립적으로 관리됩니다.

---

## 기술 스택

| 구분           | 사용 기술                      |
| ------------ | -------------------------- |
| Language     | Python 3                   |
| GUI          | PyQt5                      |
| Crawling     | Selenium                   |
| Excel        | openpyxl                   |
| Architecture | MVC + Dependency Injection |
| 기타           | 환경 변수 기반 설정 관리             |

---

## 프로젝트 구조

```text
Nubi/
├─ main.py                 # 프로그램 진입점
├─ run_gui.py              # PyQt5 GUI 실행
├─ manager/
│  └─ manager.py           # 전체 흐름 제어 매니저
├─ controller/
│  ├─ driver_controller.py
│  ├─ crawler_controller.py
│  ├─ excel_controller.py
│  ├─ timer_controller.py
│  └─ env_controller.py
├─ set/
│  ├─ driver_set.py
│  ├─ excel_set.py
│  └─ timer_set.py
├─ gui/
│  └─ ui_Nubi.py            # Qt Designer UI
├─ dependency.py            # 의존성 컨테이너
└─ resources/
   └─ res.qrc
```

---

## 동작 흐름

1. 사용자가 GUI에서

   * 사이트 선택
   * 검색어 입력
   * 검색 조건 선택
   * 페이지 수 입력
2. `manager`가 전체 흐름 제어
3. DependencyContainer를 통해

   * Timer
   * WebDriver
   * Crawler
   * Excel Controller 주입
4. 크롤링 실행
5. 결과를 Excel 객체로 반환
6. 사용자가 원하는 위치에 파일 저장

---

## 실행 방법

### 1. 필수 패키지 설치

```bash
pip install PyQt5 selenium openpyxl
```

※ Selenium 사용을 위해 ChromeDriver 등 브라우저 드라이버가 필요합니다.

---

### 2. 실행

```bash
python run_gui.py
```

---

## UI 특징

* 입력값 검증 (검색어, 조건, 페이지 수)
* 크롤링 성공 시 다운로드 버튼 활성화
* 실패 시 버튼 비활성화 및 시각적 피드백
* 저장 위치를 사용자가 직접 선택 가능

---

## 설계 특징

* 의존성 주입 구조

  * 크롤러, 드라이버, 엑셀 로직을 느슨하게 결합
* 확장성 고려

  * 신규 사이트 추가 시 Controller / Env 설정만 확장
* GUI와 비즈니스 로직 분리

  * UI 변경이 크롤링 로직에 영향 없음

---

## 향후 개선 사항

* 크롤링 진행 상태 Progress Bar 표시
* 멀티 사이트 동시 수집
* 수집 항목 사용자 선택 기능
* 로그 파일 저장
* Headless 모드 옵션 제공

---

## 라이선스

본 프로젝트는 개인 학습 및 연구 목적으로 개발되었습니다.
상업적 사용 시 사이트 정책 및 법적 이슈를 반드시 확인하시기 바랍니다.

---

원하시면 다음도 도와드릴 수 있습니다.

* README를 영문 버전으로 변환
* GitHub용 스크린샷 섹션 추가 구조 작성
* 포트폴리오용 README 톤으로 리라이팅
* 프로젝트 소개용 한 줄 설명(Short Description)

필요하신 방향을 말씀해 주시면 그에 맞게 정리해 드리겠습니다.

## 1. 웹 서비스 소개
- 웹 서비스 주제에 대한 프로젝트명과 상세 설명(선정 배경 및 문제 정의)
    - **mirror room** : 웹캠으로 사용자의 의상 실시간으로 입력받은 후 날씨를 기반으로 입고 있는 의상에 대한 조언 제공 서비스



## 2. 스토리보드 및 와이어프레임

![Team-Dashboard-Free-Resource-Shakir260](/uploads/197441594915dee79590b2a9b824d416/Team-Dashboard-Free-Resource-Shakir260.jpg)


## 3. 프로젝트 구성
1. 필요한 데이터셋
    - 엘리스에서 제공한 데이터셋 활용
    https://www.notion.so/Dataset-c7450a345d2441949d7c3541da6eb2f1


2. 기술 스택 및 라이브러리
    - 웹 서비스 제작을 위해 필요한 tool을 정리합니다.

    | 분류 | Tools | 목적 |
    | ------ | ------ | ------ |
    | Server | Flask | 웹 서버 구동 |
    | Interface | React | 사용자 인터페이스 |
    | DB | MongoDB | 데이터베이스 |



## 4. 구현 기능
- 구현해야 하는 세부 기능들을 명세하고, 우선순위를 설정합니다. 이후 우선순위를 바탕으로 개발을 진행합니다.
- 이후 구현된 기능에 알맞는 스크린샷, 영상 등을 추가합니다.
1. **필수 구현**
    - 1순위 : 이미지 업로드로 입력받은 사용자의 의상 분류
    - 2순위 : 위치에 따른 날씨 정보 기반으로 해당 의상에 대한 조언 제공
    - 3순위 : 카카오 로그인 API 적용
2. **선택 구현**
    - 1순위 : ootd 캘린더 (당일 입력받은 유저 의상을 캘린더에 사진으로 저장)
    - 2순위 : 재질에 따른 세탁방법 추천(정보제공)


## 5. 세부 일정
- 효율적인 프로젝트 수행을 위해 구현 기능의 우선순위를 바탕으로 주차별 세부 일정을 기획합니다.
- 일정은 수정될 수 있으며, 수정 시에 기획서 반영 및 팀원 공유 등을 통해 업무 관리를 합니다.
- 1주차
    - ~ 5월 14일: 기획 및 스토리보드, 와이어프레임 작성 마무리, 환경설정

** 공통 : 인공지능 모델 학습 완료 전까지는 학습 데이터 사진 및 고정된 라벨링을 통해 개발 진행**
- 2주차
    - 프론트엔드
        1. 테스트 API 완성 전 : 전체 레이아웃, 로그인, 로그아웃 화면 구성(~18일)
        1. 테스트 API 완성 후 : 위치 정보 제공 동의, 메인 기능 페이지 개발 시작
    - 백엔드
        1. 테스트 API 완성 전 : 프론트엔드 개발을 위한 백엔드 테스트 API 개발(~18일)
        1. 테스트 API 완성 후 : 카카오 로그인 및 메인 기능 페이지 관련 API 개발
    - 인공지능 학습 및 개발, 모델 중간 검토(서비스 제공, 달력, 세탁정보 제공)

- 3주차
    - 프론트엔드 : OOTD 캘린더 파트 구현
    - 백엔드 : OOTD 캘린더 파트 구현
    - 인공지능 학습 및 개발, 모델 중간 검토(서비스 제공, 달력, 세탁정보 제공) 후 메인 기능 모델 검증

- 4주차
    - 프론트엔드 : 세탁 정보 제공 파트 구현
    - 백엔드 : 세탁 정보 제공 파트 구현
    - 인공지능 학습 및 개발, 모델 중간 검토(서비스 제공, 달력, 세탁정보 제공) 후 세탁 정보 관련 모델 검증

- 5주차
    - VM 배포 및 배포상 오류 검토 및 수정
    - 최종 발표 자료 준비 및 시연 검토


## 6. 역할

| 이름 | 주 담당 업무 |
| ------ | ------ |
| 고태섭 | 백엔드 |
| 김윤주 | 백엔드 |
| 심재민 | 인공지능 |
| 윤수진 | 프론트엔드 |
| 하성민 | 프론트엔드 |



## 7. 배운 점
- 인공지능 프로젝트에서 배운 점과 느낀 점 등을 정리

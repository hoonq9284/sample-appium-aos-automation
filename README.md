## 개요
- Appium 프레임워크를 이용한 Android OS 모바일 앱 자동화 샘플 레포지토리
- Mac OS 에서의 환경 세팅 및 실행 프로세스를 제공한다.

---
## 설치 프로세스 (Mac OS)
1. Java 설치
    - `brew install openjdk`
2. node.js 설치 (npm 도 같이 설치됨)
    - `brew install node`
3. apppium 설치
    - `npm install -g appium`
4. Android Studio 설치
    - https://developer.android.com/studio/?hl=ko
    - Android Studio 를 설치하면, Android SDK 도 함께 설치됨.
    - Android Studio 에서 아래 이미지에 체크된 SDK Tool 적용![alt text](image.png)
    - Android Studio 에서 Device Manager로 가상 에뮬레이터 1개 생성
5. Android SDK 환경변수 설정
    - `vi ~/.zshrc` 명령어 입력하여 zshrc 파일 편집 모드 (i) 로 변경
    - 아래 환경변수 추가
        ```bash
        export ANDROID_SDK_ROOT=/Users/{username}/Library/Android/sdk
        export ANDROID_HOME=$ANDROID_SDK_ROOT
        export PATH=$ANDROID_SDK_ROOT:$PATH
        export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
        export PATH=$PATH:$ANDROID_SDK_ROOT/tools
        export PATH=$PATH:$ANDROID_SDK_ROOT/tools/bin
        export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
    - 추가하고, esc 키를 누른 후 `:wq` 로 저장 후 나가기
    - 나간 뒤 `source ~/.zshrc` 명령어로 파일 실행해주어야 함
6. Java 환경변수 설정
    - `vi ~/.zshrc` 명령어 입력하여 zshrc 파일 편집 모드 (i) 로 변경
    - 아래 환경변수 추가
        ```bash
        export JAVA_HOME=/Library/Java/JavaVirtualMachines/{java_version}/Content/Home
        export PATH=$PATH:$JAVA_HOME/bin
        ```
    - 추가하고, esc 키를 누른 후 `:wq` 로 저장 후 나가기
    - 나간 뒤 `source ~/.zshrc` 명령어로 파일 실행해주어야 함
7. UiAutomator2 설치
    - 설치 명령어 : `npm install -g appium-uiautomator2-driver`
    - 설치 확인 명령어 : `appium driver list --installed`
8. Appium Inspector 설치
    - `brew install --cask appium-inspector`
---
## 실행 프로세스
### 가상 디바이스에서 실행하기
1. 가상 디바이스(에뮬레이터) 를 실행한다.
    - `./run-emulator.sh`
2. behave 명령어를 실행한다.
    - `./run-behave.sh`

### 실제 단말기에서 실행하기
1. USB Port 를 이용하여 실제 안드로이드 단말기와 Mac OS 를 연결한다.
2. 안드로이드 단말기에서 개발자 옵션을 활성화한다.
3. USB 디버깅을 활성화한다.
4. behave 명령어를 실행한다.
    - `./run-behave.sh`



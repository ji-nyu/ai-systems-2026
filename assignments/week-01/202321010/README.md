# Gemini CLI 설치 과정 기록

## 1. 설치 환경

* OS: Windows + WSL (Ubuntu)
* Node.js: Node 20
* 도구: Gemini CLI (`@google/gemini-cli`)

---

## 2. 설치 과정에서 발생한 문제

### 문제 1: Node.js 버전 호환 문제

Gemini CLI 설치 시 다음과 같은 오류가 발생했다.

```
npm WARN notsup Not compatible with your version of node/npm
npm ERR! tree-sitter-bash install: node-gyp-build
npm ERR! Exit status 1
```

#### 원인

기본적으로 WSL에서 `apt install nodejs`로 설치된 Node.js 버전이 낮아
Gemini CLI에서 요구하는 Node 버전과 호환되지 않았다.

#### 해결 방법

Node.js 최신 LTS 버전을 설치하였다.

```bash
sudo apt remove nodejs npm -y
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

설치 후 버전 확인:

```bash
node -v
npm -v
```

---

### 문제 2: node-pty 모듈 빌드 실패

설치 중 다음과 같은 오류가 발생하였다.

```
node-pty optional dependency failed
tree-sitter-bash install script failed
```

#### 원인

WSL 환경에서 네이티브 모듈을 빌드하기 위한 컴파일 도구가 설치되어 있지 않았다.

#### 해결 방법

필요한 빌드 도구를 설치하였다.

```bash
sudo apt update
sudo apt install build-essential python3 make g++ -y
```

이후 Gemini CLI를 다시 설치하였다.

```bash
npm install -g @google/gemini-cli
```

---

## 3. 실행 확인

설치 후 Gemini CLI를 실행하여 정상 동작을 확인하였다.

```bash
gemini
```

Gemini CLI가 실행되며 대화형 인터페이스가 나타났다.

---

## 4. 간단한 테스트

Gemini CLI를 사용하여 hello_agent.py 파일을 생성하였다.

```python
def main():
    print("Hello from Gemini CLI!")
    print("This is a simple Python script created by your agent.")

if __name__ == "__main__":
    main()
```

실행:

```bash
python hello_agent.py
```

결과:

```
Hello from Gemini CLI!
This is a simple Python script created by your agent.
```

---

## 5. 결론

Node.js 버전 호환 문제와 빌드 도구 미설치로 인해 설치 오류가 발생하였다.
Node.js 최신 버전 설치와 필요한 빌드 도구를 추가로 설치하여 문제를 해결하였다.

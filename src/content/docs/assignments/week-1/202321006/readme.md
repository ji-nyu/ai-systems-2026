# Game Execution Guide (202321006)

이 가이드는 `uv`를 사용하여 게임을 실행하는 방법과 발생할 수 있는 문제 해결 방법을 설명합니다.

## 실행 방법

이 프로젝트는 별도의 가상 환경을 수동으로 만들 필요 없이 `uv`를 통해 즉시 실행할 수 있습니다.

### 1. 전제 조건
시스템에 `uv`가 설치되어 있어야 합니다. 설치되어 있지 않다면 다음 명령어로 설치하세요:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 게임 실행
터미널에서 해당 폴더로 이동한 후 아래 명령어를 입력하세요:
```powershell
uv run --python 3.12 --with pygame game.py
```

---

## 트러블슈팅 (Troubleshooting)

### `pygame` 빌드 오류 (`ModuleNotFoundError: No module named 'distutils'`)

**현상:**
Python 3.14 이상의 최신 버전에서 실행 시 `pygame` 설치 과정에서 다음과 같은 에러가 발생하며 빌드가 실패할 수 있습니다:
`ModuleNotFoundError: No module named 'setuptools._distutils.msvccompiler'`

**원인:**
- Python 3.12부터 `distutils`가 표준 라이브러리에서 제거되었습니다.
- 최신 Python 버전(3.14 등)에 대한 `pygame`의 미리 빌드된 바이너리(Wheel)가 아직 제공되지 않아 소스 코드를 직접 컴파일하려고 시도하게 되는데, 이 과정에서 호환성 문제가 발생합니다.

**해결 방법:**
- `uv`의 기능을 활용하여 **Python 3.12** 버전을 명시적으로 지정해 실행합니다.
- `uv`는 시스템에 해당 버전이 없더라도 자동으로 다운로드하여 격리된 환경에서 실행해 줍니다.

**실행 명령어:**
```powershell
uv run --python 3.12 --with pygame game.py
```

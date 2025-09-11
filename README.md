# Image-based Running-shoe milage estimation

# [프로젝트 이름]

> [프로젝트에 대한 한 줄 요약 설명을 작성해주세요.]
> 

## 📝 프로젝트 소개

이 프로젝트는 [프로젝트의 목표와 주요 기능에 대해 상세히 설명해주세요. 예를 들어, 'OpenCV를 활용하여 실시간 객체 인식을 구현하는 프로젝트입니다.'] 와 같은 내용을 포함할 수 있습니다.

## 👨‍💻 팀원 소개

| 이름 | 역할 | GitHub |
| --- | --- | --- |
| 양승원 | (추후 배정) | `[GitHub ID]` |
| 김현종 | (추후 배정) | `[GitHub ID]` |
| 박제준 | (추후 배정) | `[GitHub ID]` |

## 🛠️ 기술 스택

- **Language:** Python
- **Core Library:** OpenCV
- `[사용한 다른 라이브러리나 프레임워크를 추가해주세요. (e.g., TensorFlow, PyTorch, NumPy)]`

## **🚀 시작하기**

### **1. 저장소 복제 (Clone Repository)**

git clone [저장소 URL]

cd [프로젝트 폴더명]

### **2. 가상 환경 설정 및 패키지 설치**

이 프로젝트는 conda를 사용한 가상 환경을 권장합니다. [Anaconda](https://www.anaconda.com/products/distribution) 또는 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)가 설치되어 있어야 합니다.

```
# '[env-name]'라는 이름과 python 버전을 지정하여 conda 가상 환경 생성
# 프로젝트에 맞는 Python 버전을 명시해주세요. (예: python=3.9)
conda create -n [env-name] python=[version]

# 가상 환경 활성화
conda activate [env-name]

# 필요한 패키지 설치
pip install -r requirements.txt
```

> Note:
프로젝트에 필요한 패키지 목록을 requirements.txt 파일로 관리해주세요.
pip freeze > requirements.txt 명령어로 현재 환경의 패키지 목록을 생성할 수 있습니다.
>

## **▶️ 실행 방법**

프로젝트의 메인 파일을 실행하는 방법을 안내합니다.

python main.py [필요한 인자]

## **룰 & 협업 방식**

1. **브랜치 전략:**
- main: 최종 배포 버전
- develop: 개발의 중심이 되는 브랜치
- feature/기능이름: 각 기능 개발을 위한 브랜치
- fix/수정이름: 버그 수정을 위한 브랜치
2. **커밋 메시지 컨벤션:**
- [Feat]: 새로운 기능 추가
- [Fix]: 버그 수정
- [Docs]: 문서 수정
- [Style]: 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- [Refactor]: 코드 리팩토링
- [Test]: 테스트 코드, 리팩토링 테스트 코드 추가
- [Chore]: 빌드 업무 수정, 패키지 매니저 수정
> 예시: [Feat]: 로그인 기능 구현
>
3. **코드 리뷰:**
- develop 브랜치에 merge 하기 전, 최소 1명 이상의 팀원에게 코드 리뷰를 받는 것을 원칙으로 합니다. (Pull Request 사용)
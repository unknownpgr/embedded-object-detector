# Easy image detector/trainer for embedded system with OpenCV

이 프로젝트는 임베디드 시스템에서 물체 검출을 쉽게 할 수 있도록 만든 툴킷입니다.
Python3.8 이상, OpenCV python 4.8 버전에서 동작합니다.

- `collector.py`: 데이터셋을 모읍니다. 파일 상단의 `MODE`를 "true" (문자열)로 설정하고 검출하기를 원하는 오브젝트를 촬영합니다. 키보드 `s` 키를 누르면 박스 안의 이미지가 저장됩니다.
- `trainer.py`: SVM 기반 분류기를 훈련시키고 모델 파일을 생성합니다.
- `tester.py`: 모델을 테스트합니다.

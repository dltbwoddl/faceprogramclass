# faceprogramclass
teachable meachine을 통해 얼굴을 잘생김, 평범, 못생김 세가지 클래스를 학습시킨다.

얼굴만을 학습시키기 위해 웹에서 다운로드한 사진을 face_recognition을 통해 얼굴만 추출하고 색감에 의한 변화를 최소화하기 위해 흑백 변환한다.

1. high(잘생김), middle(평범), low(못생김)으로 연예인들의 사진을 분류한다. 

2. 분류한 사진을 face_recognition으로 얼굴만 추출하고 pil를 통해 grayscale로 바꾼다.
이렇게 하는 이유는 배경, 색깔의 영향을 최소화하기 위함이다.

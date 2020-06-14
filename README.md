# faceprogramclass
teachable meachine을 통해 얼굴을 잘생김, 평범, 못생김 세가지 클래스를 학습시킨다.

얼굴만을 학습시키기 위해 웹에서 다운로드한 사진을 face_recognition을 통해 얼굴만 추출하고 색감에 의한 변화를 최소화하기 위해 흑백 변환한다.

1. high(잘생김), middle(평범), low(못생김)으로 연예인들의 사진을 분류한다. 

2. 분류한 사진을 face_recognition으로 얼굴만 추출하고 pil를 통해 grayscale로 바꾼다.
이렇게 하는 이유는 배경, 색깔의 영향을 최소화하기 위함이다.

3. teachable machine을 통해 위의 이미지를 학습한 이미지 분류 인공지능을 생성한다.
https://teachablemachine.withgoogle.com/train/image
클라우드 상에 업로드된 모델 주소 : https://teachablemachine.withgoogle.com/models/AkdcNn9tB/

4.웹페이지를 생성한다.(js, codepen, bootstrap, netlify 등을 활용)

웹 페이지 주소 : https://naughty-noether-a8b46b.netlify.app/
#보다 상세한 정보는 코드에서 확인해 주세요.
학습 데이터에 포함되지 않은 강다니엘씨를 넣어보았습니다.
결과가 challenger인 것을 보면 나름 정확한 것 같네요.
물론 아직 완벽하지 않습니다.
![alt text](https://dltbwoddl.github.io/faceprogramclass/result.png)
부족한 점 : high, middle, low를 사람이 직접 분류하기 때문에 학습데이터에 편향이 있을 수 있다.
또한 잘생김, 평범, 못생김을 나누는 기준이 매우 다양하기 때문에 매우 많은 데이터를 요구한다. 하지만 500여개의 데이터만 확보해 정확도가 그다지 높지 않다.
코드적인 부분에서는 js, css를 분류하지 못했고 코드가 전체적으로 깔끔하지 못하다.

import streamlit as st
import pandas as pd
import requests
import os

def get_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return "Unknown"

st.title("2-10반 소리함")

a = st.text_area("2-10반 회장에게 말하고 싶은 말 *")
b = st.text_area("2-10반에게 문의하고 싶은것 *")
c = st.text_input("이름")
st.code("""개인정보 처리방침
소리함(이하 "서비스")은 이용자의 개인정보를 중요시하며, 다음과 같은 방침에 따라 개인정보를 수집·이용·보관·파기합니다. 본 방침은 관련 법령에 따라 수시로 변경될 수 있으며, 변경 시 본 서비스 내에서 공지합니다.

1. 수집하는 개인정보 항목
서비스는 아래의 개인정보를 수집합니다:

의견 내용 (필수)

이름 (선택)

접속 IP 주소 (자동 수집)

2. 개인정보 수집 목적
수집한 개인정보는 아래의 목적을 위해 사용됩니다:

의견에 대한 분석 및 서비스 개선

서비스 운영의 안정성 확보 및 악용 방지

3. 개인정보 보유 및 이용기간
수집된 개인정보는 의견 접수일로부터 1년간 보관 후 안전하게 파기됩니다. 단, 관계법령에 의해 보존할 필요가 있는 경우 해당 법령에 따릅니다.

4. 개인정보의 제3자 제공
서비스는 이용자의 개인정보를 제3자에게 제공하지 않습니다. 다만, 법령에 의해 요구되는 경우에는 예외로 합니다.

5. 개인정보의 파기 절차 및 방법
보유 기간이 경과하거나 수집 목적이 달성된 개인정보는 즉시 파기합니다. 전자적 파일은 복구할 수 없는 기술적 방법으로 삭제하며, 출력물은 분쇄 또는 소각을 통해 파기합니다.

6. 이용자의 권리
이용자는 언제든지 자신의 개인정보에 대해 열람, 정정, 삭제를 요청할 수 있습니다. 요청은 서비스 내 문의를 통해 접수받습니다.

7. 개인정보 보호책임자
책임자: 이지호

연락처: leejiho1531@naver.com""")
agree = st.checkbox(f"나는 개인정보 처리방침에 동의합니다.")
if agree:
    if st.button("전송"):
        if a and b:
            ip = get_ip()
            new_data = pd.DataFrame([{'회장에게': a, '반에': b, '이름': c, 'ip': ip}])
            
            # 파일이 존재하면 이어쓰기, 없으면 새로 생성
            file_path = 'soriham.csv'  # 또는 'soriham.scv' 도 가능
            if os.path.exists(file_path):
                existing = pd.read_csv(file_path)
                combined = pd.concat([existing, new_data], ignore_index=True)
            else:
                combined = new_data

            combined.to_csv(file_path, index=False)
            st.toast('전송되었습니다!', icon='🎉')
        else:
            st.warning("정보를 입력해주세요.")

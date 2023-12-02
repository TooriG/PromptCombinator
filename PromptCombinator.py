import streamlit as st

def combine_text(list1, list2):
    combined_list = [f"{item1}, {item2}" for item1 in list1 for item2 in list2]
    return "\n".join(combined_list)

# Streamlitアプリの設定
st.title("テキスト組み合わせアプリ")

# 入力1（改行で分割されたテキスト）
input_text1 = st.text_area("入力1（行ごとに改行）", value="aaaa\nbbbb\ncccc", height=100)

# 入力2（同様に改行で分割）
input_text2 = st.text_area("入力2（行ごとに改行）", value="1111\n2222\n3333\n4444", height=100)

# 組み合わせボタン
if st.button("組み合わせる"):
    # 入力テキストを行で分割
    list1 = input_text1.split("\n")
    list2 = input_text2.split("\n")
    
    # 組み合わせを行い、結果を表示
    combined_text = combine_text(list1, list2)
    st.text_area("結果", value=combined_text, height=300)

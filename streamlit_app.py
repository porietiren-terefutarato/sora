# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('君の悪魔の実')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('おまえの二つ名を入力しろ！')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示

# スライダーを作成し、値を選択
number = st.slider('今の懸賞金を教えろ', 0, 10000000000)

# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")

# 選択した数字を表示
st.write(f'お前の懸賞金は「{number}」だな')

with st.spinner("ちょいまち"):
    time.sleep(2)
st.write("わかったぞ")    

if (number<=50):
    st.write("実なしｗ")
if (50<number<=10000000)：
    st.write("君の悪魔の実は「アワアワの実」だ！！")
if (10000000<number<=50000000):
    st.write("君の悪魔の実は「ツルツルの実」だ！！")
if (50000000<number<=500000000):
    st.write("君の悪魔の実は「バネバネの実」だ！！")
    

# 選択した数値を2進数に変換
binary_representation = bin(number)[2:]  # 'bin'関数で2進数に変換し、先頭の'0b'を取り除く
st.info(f'🔢 10進数の「{number}」を2進数で表現すると「{binary_representation}」になります。 🔢')  # 2進数の表示をハイライト

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="منصة رافت - نموذج تداول", layout="wide")

st.title("📊 منصة رافت - نموذج لواجهة تداول مباشر")

st.markdown("""
مرحباً، هذا نموذج مبدئي بسيط لعرض واجهة نظام تداول مباشر يربط بيانات من Binance وTradingView،
بهدف توضيح تجربة المستخدم وتقديم البيانات بشكل تفاعلي وسلس.
""")

st.subheader("📈 بيانات أسعار مباشرة (عينة)")
data = {
    "العملة": ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT"],
    "السعر الحالي ($)": [31250, 2050, 312, 85],
    "تغير 24h (%)": [1.2, -0.5, 0.8, 3.5],
    "حجم التداول (M)": [2500, 1800, 920, 430]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("📊 نظرة على الاتجاه العام")
days = pd.date_range(datetime.today() - timedelta(days=30), periods=30)
prices = np.cumsum(np.random.randn(30)) + 31000

fig, ax = plt.subplots()
ax.plot(days, prices, color='green')
ax.set_title("سعر BTC/USDT - حركة وهمية آخر 30 يوم")
ax.set_ylabel("السعر بالدولار")
ax.set_xlabel("التاريخ")
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("🚀 نموذج إشارة تداول (تجريبي)")
with st.form("trade_signal_form"):
    pair = st.selectbox("اختر الزوج:", ["BTC/USDT", "ETH/USDT", "BNB/USDT"])
    action = st.radio("نوع الإشارة:", ["شراء", "بيع"])
    note = st.text_input("ملاحظة (اختياري)")
    submitted = st.form_submit_button("إرسال")
    if submitted:
        st.success(f"تم استلام إشارة {action} على {pair} ✔️")

st.markdown("""
---

### ⚙️ ملاحظات تقنية:
- يمكن ربط هذه الواجهة مع Binance API لعرض بيانات حقيقية.
- نقدر ندمج TradingView Charts بشكل حي.
- نضيف Webhooks أو تنبيهات Telegram حسب الحاجة.
- التصميم قابل للتطوير ليشمل تسجيل دخول، إدارة محافظ، ومتابعة تلقائية.

""")

st.markdown("📞 للتواصل أو طلب النسخة الكاملة: [اضغط هنا](https://wa.me/+972569804786)")

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="منصة رافت - واجهة تداول مباشرة", layout="wide")

st.title("📊 منصة رافت - نموذج لواجهة تداول مباشرة")

st.markdown("""
نموذج مبسّط لعرض بيانات سوق العملات الرقمية باستخدام TradingView وبيانات محدثة،
مصمم لتوفير تجربة مستخدم عملية وسريعة لمتابعة التداول.
""")

# واجهة TradingView
st.subheader("📺 واجهة TradingView الحية")
components.html("""
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
  "width": "100%",
  "height": "1500",
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "allow_symbol_change": true,
  "support_host": "https://www.tradingview.com"
}
  </script>
</div>
""", height=1200)

# جدول بيانات الأسعار
st.subheader("📈 بيانات أسعار (تجريبية)")
data = {
    "العملة": ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT"],
    "السعر الحالي ($)": [31250, 2050, 312, 85],
    "تغير 24h (%)": [1.2, -0.5, 0.8, 3.5],
    "حجم التداول (M)": [2500, 1800, 920, 430]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("""
---
📌 **ملاحظات تقنية**:
- الكود قابل للتوسيع ليشمل ربط مباشر مع Binance API
- يمكن تعديل TradingView لعرض أي عملة أو مؤشر فوري
- قابل لإضافة تسجيل دخول أو إشعارات تداول بسهولة
""")

st.markdown("📞 للتواصل أو تجربة مخصصة: [اضغط هنا](https://wa.me/+972569804786)")

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
<div class="tradingview-widget-container" style="height:820px;width:100%">
  <div class="tradingview-widget-container__widget" style="height:100%;width:100%"></div>
  <div class="tradingview-widget-copyright">
    <a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank">
      <span class="blue-text">تابع السوق مباشرة على TradingView</span>
    </a>
  </div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
    "autosize": true,
    "symbol": "BINANCE:BTCUSDT",
    "interval": "30",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "ar",
    "enable_publishing": false,
    "withdateranges": true,
    "allow_symbol_change": true,
    "calendar": false,
    "support_host": "https://www.tradingview.com"
  }
  </script>
</div>
""", height=820)

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

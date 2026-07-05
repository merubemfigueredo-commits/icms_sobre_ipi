import streamlit as st

st.set_page_config(page_title="ICMS sobre IPI e IPI sobre ICMS", page_icon="🧮", layout="centered")

st.title("ICMS sobre IPI e IPI sobre ICMS")
st.caption('Cálculo de ICMS "por dentro" com IPI integrado.')

with st.form("icms_form"):
    custo = st.number_input("Custo sem ICMS (R$)", min_value=0.0, step=0.01, format="%.2f")
    col1, col2 = st.columns(2)
    with col1:
        icms = st.number_input("Alíquota ICMS (%)", min_value=0.0, max_value=100.0, value=18.0, step=0.01, format="%.2f")
    with col2:
        ipi = st.number_input("Alíquota IPI (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.01, format="%.2f")

    calcular = st.form_submit_button("Calcular", use_container_width=True)

if calcular:
    if custo <= 0:
        st.warning("Informe um custo de produto maior que zero.")
    else:
        x = icms / 100
        y = ipi / 100
        denominador = 1 - x - (x * y)

        if denominador <= 0:
            st.error("As alíquotas informadas são muito altas e o cálculo é impossível.")
        else:
            valor_icms = ((x + (x * y)) / denominador) * custo
            custo_total = custo + valor_icms

            st.divider()
            st.subheader("Resumo do Cálculo")

            col1, col2, col3 = st.columns(3)
            col1.metric("Custo Inicial", f"R$ {custo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            col2.metric("ICMS Apurado", f"R$ {valor_icms:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            col3.metric("Custo Final", f"R$ {custo_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            st.caption(f"Alíquota ICMS: {icms:.2f}%  |  Alíquota IPI: {ipi:.2f}%")

with st.expander("Entenda o ICMS por dentro"):
    st.write(
        "O **ICMS por dentro** é uma particularidade da legislação brasileira onde o próprio imposto "
        "compõe a sua base de cálculo. Isso significa que o valor destacado na nota fiscal é embutido "
        "no custo final, garantindo que a margem da empresa não seja consumida pelo imposto quando a "
        "alíquota é aplicada sobre o valor total."
    )

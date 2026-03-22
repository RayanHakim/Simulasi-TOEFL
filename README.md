import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# Import database soal
from data_grammar import db_grammar
from data_reading import db_reading

# Import materi (File Baru!)
from materi_grammar import grammar_content
from materi_reading import reading_content

st.set_page_config(page_title="Simulasi TOEFL", page_icon="🎯", layout="wide")

# --- SIDEBAR MENU NAVIGATION ---
st.sidebar.title("📌 Menu Navigasi")
menu = st.sidebar.radio("Pilih Mode:", ["📚 Modul Materi", "🎯 Simulasi Tes"])
st.sidebar.markdown("---")

if menu == "📚 Modul Materi":
    st.title("📚 Pusat Materi TOEFL")
    st.info("Pahami pola dan algoritma soal di sini sebelum memulai simulasi.")
    
    tab_mat_read, tab_mat_gram = st.tabs(["📖 Reading Tips & Vocab", "📝 Grammar Rules"])
    
    with tab_mat_read:
        st.markdown(reading_content)
        
    with tab_mat_gram:
        st.markdown(grammar_content)

elif menu == "🎯 Simulasi Tes":
    # -- LOGIKA TIMER REAL-TIME --
    if st.session_state.get('started') and not st.session_state.get('submitted'):
        st_autorefresh(interval=1000, key="datetimer")

    if 'started' not in st.session_state:
        st.session_state.started = False
        st.session_state.start_time = None
        st.session_state.selected_grammar = []
        st.session_state.selected_reading = []
        st.session_state.answers = {}
        st.session_state.submitted = False

    def start_simulasi():
        st.session_state.started = True
        st.session_state.submitted = False
        st.session_state.start_time = time.time()
        
        n_grammar = min(len(db_grammar), 50)
        n_reading = min(len(db_reading), 50)
        
        st.session_state.selected_grammar = random.sample(db_grammar, n_grammar)
        st.session_state.selected_reading = random.sample(db_reading, n_reading)
        st.session_state.answers = {}

    st.title("🚀 Simulasi TOEFL")
    st.markdown("---")

    if not st.session_state.started:
        st.info(f"Database terdeteksi: {len(db_grammar)} soal Grammar, {len(db_reading)} soal Reading.")
        st.write("Sistem akan mengambil maksimal 50 soal per kategori secara acak.")
        
        if st.button("MULAI TES SEKARANG", type="primary"):
            start_simulasi()
            st.rerun()

    elif st.session_state.started and not st.session_state.submitted:
        now = time.time()
        elapsed = int(now - st.session_state.start_time)
        limit = 115 * 60  # 115 Menit
        remaining = limit - elapsed

        if remaining <= 0:
            st.error("🚨 WAKTU HABIS! Mengirim jawaban otomatis...")
            st.session_state.submitted = True
            st.rerun()
        
        mins, secs = divmod(remaining, 60)
        
        st.sidebar.header("⏱️ LIVE TIMER")
        st.sidebar.subheader(f"{mins:02d} Menit {secs:02d} Detik")
        st.sidebar.progress(max(0, remaining) / limit)

        tab1, tab2 = st.tabs(["📝 Grammar", "📖 Reading"])

        with tab1:
            for i, q in enumerate(st.session_state.selected_grammar):
                st.markdown(f"**{i+1}.** {q['soal']}")
                st.session_state.answers[f"g_{i}"] = st.radio(f"G_{i}", q['pilihan'], index=None, key=f"key_g_{i}", label_visibility="collapsed")
                st.write("")

        with tab2:
            for i, q in enumerate(st.session_state.selected_reading):
                st.info(f"**PASSAGE:** {q['passage']}")
                st.markdown(f"**{i+1}.** {q['soal']}")
                st.session_state.answers[f"r_{i}"] = st.radio(f"R_{i}", q['pilihan'], index=None, key=f"key_r_{i}", label_visibility="collapsed")
                st.divider()

        if st.button("SUBMIT SEMUA JAWABAN", type="primary"):
            st.session_state.submitted = True
            st.rerun()

    elif st.session_state.submitted:
        st.header("📊 Hasil Evaluasi")
        
        g_correct = 0
        for i, q in enumerate(st.session_state.selected_grammar):
            ans = st.session_state.answers.get(f"g_{i}")
            if ans and ans.startswith(q['jawaban']):
                g_correct += 1
                
        r_correct = 0
        for i, q in enumerate(st.session_state.selected_reading):
            ans = st.session_state.answers.get(f"r_{i}")
            if ans and ans.startswith(q['jawaban']):
                r_correct += 1

        total_score = g_correct + r_correct
        max_score = len(st.session_state.selected_grammar) + len(st.session_state.selected_reading)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Skor Grammar", f"{g_correct}/{len(st.session_state.selected_grammar)}")
        col2.metric("Skor Reading", f"{r_correct}/{len(st.session_state.selected_reading)}")
        col3.metric("Total Benar", f"{total_score}/{max_score}")

        with st.expander("Lihat Kunci Jawaban Lengkap"):
            st.write("### Kunci Grammar")
            for i, q in enumerate(st.session_state.selected_grammar):
                st.write(f"**{i+1}.** {q['soal']} | **Kunci:** {q['jawaban']}")
            
            st.write("### Kunci Reading")
            for i, q in enumerate(st.session_state.selected_reading):
                st.write(f"**{i+1}.** {q['soal']} | **Kunci:** {q['jawaban']}")

        if st.button("Ulangi Tes"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


import streamlit as st
import pandas as pd
import joblib


# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="NEXUS IDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOAD MODELS
# =========================================================

@st.cache_resource
def load_models():

    model = joblib.load("ensemble_model.pkl")
    target_encoder = joblib.load("target_encoder.pkl")
    onehot_encoder = joblib.load("onehot_encoder.pkl")
    scaler = joblib.load("scaler.pkl")
    columns = joblib.load("columns.pkl")

    return model, target_encoder, onehot_encoder, scaler, columns


model, target_encoder, onehot_encoder, scaler, columns = load_models()


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Rajdhani:wght@400;500;600;700&display=swap');


/* =========================
   GLOBAL
   ========================= */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0,255,170,0.07), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(0,170,255,0.06), transparent 25%),
        linear-gradient(135deg, #05080c 0%, #081016 50%, #05080c 100%);
    color: #e6edf3;
    font-family: 'Rajdhani', sans-serif;
}


#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* =========================
   SIDEBAR
   ========================= */

[data-testid="stSidebar"] {
    background: #060a0f;
    border-right: 1px solid #16252b;
}

[data-testid="stSidebar"] * {
    font-family: 'Rajdhani', sans-serif;
}


/* =========================
   HEADINGS
   ========================= */

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
}


/* =========================
   MAIN HEADER
   ========================= */

.hero {
    padding: 10px 0 20px 0;
}

.logo {
    font-family: 'Orbitron';
    font-size: 15px;
    letter-spacing: 5px;
    color: #00ffaa;
}

.hero-title {
    font-family: 'Orbitron';
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 8px;
}

.hero-subtitle {
    color: #6e7d87;
    font-size: 17px;
    letter-spacing: 1px;
}


/* =========================
   STATUS
   ========================= */

.status {
    background: rgba(0,255,170,0.04);
    border: 1px solid rgba(0,255,170,0.25);
    border-radius: 12px;
    padding: 14px;
    text-align: center;
}

.status-dot {
    color: #00ffaa;
    font-size: 14px;
}

.status-text {
    color: #00ffaa;
    font-weight: 700;
    letter-spacing: 2px;
}


/* =========================
   METRIC CARDS
   ========================= */

.card {
    background: linear-gradient(
        145deg,
        rgba(17,28,35,0.95),
        rgba(7,13,18,0.95)
    );

    border: 1px solid #172a31;
    border-radius: 16px;
    padding: 20px;

    box-shadow:
        0 0 25px rgba(0,255,170,0.025),
        inset 0 0 20px rgba(255,255,255,0.01);

    transition: 0.25s;
}

.card:hover {
    border-color: rgba(0,255,170,0.4);
    box-shadow:
        0 0 25px rgba(0,255,170,0.08);
}

.card-label {
    color: #65747e;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.card-value {
    font-family: 'Orbitron';
    font-size: 27px;
    margin-top: 8px;
    color: #e9fff8;
}

.card-small {
    color: #00ffaa;
    font-size: 13px;
    margin-top: 5px;
}


/* =========================
   SECTION
   ========================= */

.section {
    margin-top: 28px;
    margin-bottom: 12px;

    font-family: 'Orbitron';
    font-size: 16px;
    letter-spacing: 2px;

    color: #dce8ed;

    border-left: 3px solid #00ffaa;
    padding-left: 12px;
}


/* =========================
   EXPANDERS
   ========================= */

[data-testid="stExpander"] {
    background: rgba(8,15,20,0.75);
    border: 1px solid #172a31;
    border-radius: 14px;
    margin-bottom: 10px;
}

[data-testid="stExpander"]:hover {
    border-color: rgba(0,255,170,0.35);
}


/* =========================
   INPUTS
   ========================= */

input, textarea {
    background: #0a1117 !important;
    color: #dce8ed !important;
    border: 1px solid #1b3038 !important;
    border-radius: 9px !important;
}

label {
    color: #83939c !important;
    font-size: 13px !important;
}


/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {
    background: #0a1117 !important;
    border: 1px solid #1b3038 !important;
    border-radius: 9px !important;
}


/* =========================
   BUTTON
   ========================= */

.stButton > button {
    height: 60px;

    background:
        linear-gradient(
            90deg,
            #00a878,
            #00ffaa
        );

    color: #02100b;

    border: none;
    border-radius: 12px;

    font-family: 'Orbitron';
    font-size: 16px;
    font-weight: 800;

    letter-spacing: 2px;

    box-shadow:
        0 0 25px rgba(0,255,170,0.18);

    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 0 40px rgba(0,255,170,0.35);
}


/* =========================
   NORMAL RESULT
   ========================= */

.normal {
    background:
        radial-gradient(
            circle at center,
            rgba(0,255,170,0.12),
            rgba(0,255,170,0.02)
        );

    border: 1px solid rgba(0,255,170,0.5);

    border-radius: 20px;

    padding: 35px;

    text-align: center;

    box-shadow:
        0 0 50px rgba(0,255,170,0.08);
}


/* =========================
   ATTACK RESULT
   ========================= */

.attack {
    background:
        radial-gradient(
            circle at center,
            rgba(255,45,85,0.16),
            rgba(255,45,85,0.02)
        );

    border: 1px solid rgba(255,45,85,0.6);

    border-radius: 20px;

    padding: 35px;

    text-align: center;

    box-shadow:
        0 0 50px rgba(255,45,85,0.10);
}


.result-icon {
    font-size: 45px;
}

.result-title {
    font-family: 'Orbitron';
    font-size: 30px;
    font-weight: 800;
    margin-top: 10px;
}

.result-subtitle {
    color: #73828c;
    font-size: 16px;
    margin-top: 8px;
}


/* =========================
   TERMINAL
   ========================= */

.terminal {
    background: #030607;
    border: 1px solid #172a31;
    border-radius: 12px;
    padding: 18px;

    font-family: monospace;
    font-size: 13px;

    color: #00ffaa;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-family:Orbitron;
            font-size:20px;
            color:#00ffaa;
            letter-spacing:2px;
            margin-bottom:25px;
        ">
        🛡️ NEXUS IDS
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### SYSTEM")

    st.success("● SYSTEM ONLINE")

    st.write("")

    st.markdown("**MODEL**")
    st.write("Voting Ensemble")

    st.markdown("**ALGORITHMS**")
    st.write("Logistic Regression")
    st.write("Decision Tree")
    st.write("Random Forest")

    st.markdown("**DATASET**")
    st.write("UNSW-NB15")

    st.markdown("**FEATURES**")
    st.write("34 Network Features")

    st.divider()

    st.caption("NEXUS IDS v1.0")


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="logo">
            NEXUS // SECURITY OPERATIONS
        </div>

        <div class="hero-title">
            NETWORK INTRUSION DETECTION
        </div>

        <div class="hero-subtitle">
            AI-powered threat analysis using UNSW-NB15
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# STATUS ROW
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="status">
            <span class="status-dot">●</span>
            <span class="status-text"> SYSTEM ONLINE</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="status">
            MODEL<br>
            <b>VOTING ENSEMBLE</b>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="status">
            DATASET<br>
            <b>UNSW-NB15</b>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="status">
            FEATURES<br>
            <b>34 ACTIVE</b>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# TOP CARDS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">Detection Engine</div>
            <div class="card-value">AI / ML</div>
            <div class="card-small">ACTIVE</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">Models</div>
            <div class="card-value">03</div>
            <div class="card-small">ENSEMBLED</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">Input Features</div>
            <div class="card-value">34</div>
            <div class="card-small">NETWORK SIGNALS</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">Classification</div>
            <div class="card-value">BINARY</div>
            <div class="card-small">NORMAL / ATTACK</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# INPUT SECTIONS
# =========================================================

st.markdown(
    '<div class="section">◈ TRAFFIC TELEMETRY</div>',
    unsafe_allow_html=True
)


# =========================================================
# CONNECTION
# =========================================================

with st.expander("🔗  CONNECTION INTELLIGENCE", expanded=True):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        dur = st.number_input("Duration", value=0.0)

    with c2:
        proto = st.selectbox(
            "Protocol",
            ["tcp", "udp", "icmp", "arp", "ospf", "other"]
        )

    with c3:
        service = st.text_input("Service", value="-")

    with c4:
        state = st.selectbox(
            "Connection State",
            [
                "FIN",
                "CON",
                "REQ",
                "RST",
                "ACC",
                "CLO",
                "INT",
                "ECO",
                "PAR"
            ]
        )


# =========================================================
# PACKETS
# =========================================================

with st.expander("📦  PACKET & BYTE TELEMETRY"):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        spkts = st.number_input(
            "Source Packets",
            min_value=0,
            value=1
        )

    with c2:
        dpkts = st.number_input(
            "Destination Packets",
            min_value=0,
            value=1
        )

    with c3:
        sbytes = st.number_input(
            "Source Bytes",
            min_value=0,
            value=0
        )

    with c4:
        dbytes = st.number_input(
            "Destination Bytes",
            min_value=0,
            value=0
        )

    c1, c2 = st.columns(2)

    with c1:
        sloss = st.number_input(
            "Source Loss",
            value=0.0
        )

    with c2:
        dloss = st.number_input(
            "Destination Loss",
            value=0.0
        )


# =========================================================
# TRAFFIC
# =========================================================

with st.expander("⚡  TRAFFIC FLOW & LOAD"):

    c1, c2, c3 = st.columns(3)

    with c1:
        rate = st.number_input(
            "Rate",
            value=0.0
        )

    with c2:
        sload = st.number_input(
            "Source Load",
            value=0.0
        )

    with c3:
        dload = st.number_input(
            "Destination Load",
            value=0.0
        )


# =========================================================
# TIMING
# =========================================================

with st.expander("⏱️  TIMING & JITTER"):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        sinpkt = st.number_input(
            "Source Packet Interval",
            value=0.0
        )

    with c2:
        dinpkt = st.number_input(
            "Destination Packet Interval",
            value=0.0
        )

    with c3:
        sjit = st.number_input(
            "Source Jitter",
            value=0.0
        )

    with c4:
        djit = st.number_input(
            "Destination Jitter",
            value=0.0
        )


# =========================================================
# TCP
# =========================================================

with st.expander("🌐  TCP SECURITY TELEMETRY"):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        swin = st.number_input(
            "Source Window",
            value=0
        )

    with c2:
        stcpb = st.number_input(
            "Source TCP Base",
            value=0
        )

    with c3:
        dtcpb = st.number_input(
            "Destination TCP Base",
            value=0
        )

    with c4:
        dwin = st.number_input(
            "Destination Window",
            value=0
        )

    c1, c2, c3 = st.columns(3)

    with c1:
        tcprtt = st.number_input(
            "TCP RTT",
            value=0.0
        )

    with c2:
        synack = st.number_input(
            "SYN-ACK",
            value=0.0
        )

    with c3:
        ackdat = st.number_input(
            "ACK Data",
            value=0.0
        )


# =========================================================
# PACKET SIZE
# =========================================================

with st.expander("📏  PACKET SIZE ANALYTICS"):

    c1, c2 = st.columns(2)

    with c1:
        smean = st.number_input(
            "Source Mean",
            value=0.0
        )

    with c2:
        dmean = st.number_input(
            "Destination Mean",
            value=0.0
        )


# =========================================================
# CONNECTION BEHAVIOR
# =========================================================

with st.expander("🔎  CONNECTION BEHAVIOR"):

    c1, c2, c3 = st.columns(3)

    with c1:
        trans_depth = st.number_input(
            "Transaction Depth",
            value=0
        )

    with c2:
        response_body_len = st.number_input(
            "Response Body Length",
            value=0
        )

    with c3:
        ct_src_dport_ltm = st.number_input(
            "Source → Destination Port Connections",
            value=0
        )

    ct_dst_sport_ltm = st.number_input(
        "Destination → Source Port Connections",
        value=0
    )


# =========================================================
# APPLICATION
# =========================================================

with st.expander("📡  APPLICATION / FTP / HTTP"):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        is_ftp_login = st.number_input(
            "FTP Login",
            min_value=0,
            max_value=1,
            value=0
        )

    with c2:
        ct_ftp_cmd = st.number_input(
            "FTP Commands",
            value=0
        )

    with c3:
        ct_flw_http_mthd = st.number_input(
            "HTTP Methods",
            value=0
        )

    with c4:
        is_sm_ips_ports = st.number_input(
            "Same IP / Port",
            min_value=0,
            max_value=1,
            value=0
        )


# =========================================================
# ANALYZE
# =========================================================

st.write("")

st.markdown(
    '<div class="section">◈ THREAT ANALYSIS ENGINE</div>',
    unsafe_allow_html=True
)

detect = st.button(
    "🚀  ANALYZE NETWORK TRAFFIC",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if detect:

    data = pd.DataFrame({

        "dur": [dur],
        "proto": [proto],
        "service": [service],
        "state": [state],

        "spkts": [spkts],
        "dpkts": [dpkts],

        "sbytes": [sbytes],
        "dbytes": [dbytes],

        "rate": [rate],
        "sload": [sload],
        "dload": [dload],

        "sloss": [sloss],
        "dloss": [dloss],

        "sinpkt": [sinpkt],
        "dinpkt": [dinpkt],

        "sjit": [sjit],
        "djit": [djit],

        "swin": [swin],
        "stcpb": [stcpb],
        "dtcpb": [dtcpb],
        "dwin": [dwin],

        "tcprtt": [tcprtt],
        "synack": [synack],
        "ackdat": [ackdat],

        "smean": [smean],
        "dmean": [dmean],

        "trans_depth": [trans_depth],
        "response_body_len": [response_body_len],

        "ct_src_dport_ltm": [ct_src_dport_ltm],
        "ct_dst_sport_ltm": [ct_dst_sport_ltm],

        "is_ftp_login": [is_ftp_login],
        "ct_ftp_cmd": [ct_ftp_cmd],
        "ct_flw_http_mthd": [ct_flw_http_mthd],
        "is_sm_ips_ports": [is_sm_ips_ports]
    })


    # =====================================================
    # ENCODING
    # =====================================================

    data["proto"] = target_encoder.transform(
        data[["proto"]]
    ).ravel()


    encoded = onehot_encoder.transform(
        data[["service", "state"]]
    )
    encoded_df = pd.DataFrame(
        encoded,
        columns=onehot_encoder.get_feature_names_out(
            ["service", "state"]
        ),
        index=data.index
    )


    data = pd.concat(
        [
            data.drop(
                columns=["service", "state"]
            ),
            encoded_df
        ],
        axis=1
    )


    # =====================================================
    # ALIGN COLUMNS
    # =====================================================

    data = data.reindex(
        columns=columns,
        fill_value=0
    )


    # =====================================================
    # SCALE
    # =====================================================

    data_scaled = scaler.transform(data)


    # =====================================================
    # PREDICT
    # =====================================================

    prediction = model.predict(data_scaled)[0]

    probability = model.predict_proba(
        data_scaled
    )[0][1]

    normal_probability = 1 - probability


    # =====================================================
    # RESULT
    # =====================================================

    st.write("")

    if prediction == 1:

        st.markdown(
            f"""
            <div class="attack">

                <div class="result-icon">
                    🚨
                </div>

                <div class="result-title">
                    THREAT DETECTED
                </div>

                <div class="result-subtitle">
                    Malicious network activity identified
                </div>

                <br>

                <div style="
                    font-family:Orbitron;
                    font-size:38px;
                    color:#ff4567;
                ">
                    {probability * 100:.2f}%
                </div>

                <div class="result-subtitle">
                    ATTACK PROBABILITY
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="normal">

                <div class="result-icon">
                    🟢
                </div>

                <div class="result-title">
                    SYSTEM CLEAR
                </div>

                <div class="result-subtitle">
                    No malicious network activity detected
                </div>

                <br>

                <div style="
                    font-family:Orbitron;
                    font-size:38px;
                    color:#00ffaa;
                ">
                    {normal_probability * 100:.2f}%
                </div>

                <div class="result-subtitle">
                    NORMAL PROBABILITY
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # PROBABILITY
    # =====================================================

    st.write("")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            """
            <div class="card">
                <div class="card-label">
                    NORMAL TRAFFIC
                </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            "Probability",
            f"{normal_probability * 100:.2f}%"
        )

        st.progress(
            float(normal_probability)
        )

        st.markdown("</div>", unsafe_allow_html=True)


    with c2:

        st.markdown(
            """
            <div class="card">
                <div class="card-label">
                    ATTACK TRAFFIC
                </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            "Probability",
            f"{probability * 100:.2f}%"
        )

        st.progress(
            float(probability)
        )

        st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # TERMINAL
    # =====================================================

    st.write("")

    st.markdown(
        f"""
        <div class="terminal">

        > NEXUS IDS :: ANALYSIS COMPLETE<br>
        > MODEL :: VOTING ENSEMBLE<br>
        > FEATURES :: 34<br>
        > PREDICTION :: {"ATTACK" if prediction == 1 else "NORMAL"}<br>
        > ATTACK SCORE :: {probability * 100:.2f}%<br>
        > STATUS :: {"THREAT DETECTED" if prediction == 1 else "SYSTEM CLEAR"}<br>
        > ENGINE :: ONLINE

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#46545d;
        font-family:Orbitron;
        font-size:11px;
        letter-spacing:2px;
    ">
        NEXUS IDS • UNSW-NB15 • MACHINE LEARNING SECURITY ENGINE
    </div>
    """,
    unsafe_allow_html=True
)

import base64
import os
import streamlit as st

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="English Listening Center", page_icon="🎧", layout="wide"
)

# Custom CSS canh lề chuẩn cho 2 cột Script & Dịch
st.markdown(
    """
<style>
    .main-header { text-align: center; margin-bottom: 30px; }
    .author-badge { 
        display: inline-block; background-color: #eff6ff; color: #2563eb; 
        font-weight: 700; padding: 6px 16px; border-radius: 9999px; 
        border: 1px solid #dbeafe; margin-top: 5px; 
    }
    
    /* Khung chuẩn hóa cho Script Tiếng Anh & Dịch Tiếng Việt */
    .script-box {
        min-height: 100%;
        padding: 16px;
        border-radius: 10px;
        font-size: 0.95rem;
        line-height: 1.7;
        white-space: pre-wrap;
        box-sizing: border-box;
    }
    
    .script-en {
        color: #1e293b;
        background-color: #f8fafc;
        border-left: 4px solid #3b82f6;
    }
    
    .script-vi {
        color: #047857;
        font-style: italic;
        background-color: #f0fdf4;
        border-left: 4px solid #10b981;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Hàm mã hóa file audio local thành base64
def get_audio_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# Sidebar bộ lọc bài nghe
st.sidebar.header("🔍 Lọc bài nghe")
search_term = st.sidebar.text_input("Tìm kiếm theo tên hoặc từ khóa:", "")

# Ví dụ hiển thị bài nghe với bố cục canh lề chuẩn
for lesson in LESSONS:
    if search_term.lower() in lesson["title"].lower() or search_term.lower() in str(
        lesson["id"]
    ):
        with st.container():
            st.markdown(
                f"### Bài {lesson['id']}. {lesson['icon']} {lesson['title']} `{lesson['file']}`"
            )

            audio_path = os.path.join("audio", lesson["file"])
            b64_audio = get_audio_base64(audio_path)

            if b64_audio:
                audio_html = f"""
                <div style="background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 10px;">
                    <audio id="audio_{lesson['id']}" controls style="width: 100%;">
                        <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
                    </audio>
                    
                    <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; flex-wrap: wrap;">
                        <span style="font-weight: 600; font-size: 0.85rem; color: #64748b;">Tốc độ:</span>
                        <button onclick="setSpeed({lesson['id']}, 0.75)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #fff; cursor: pointer;">0.75x</button>
                        <button onclick="setSpeed({lesson['id']}, 0.8)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #fff; cursor: pointer;">0.8x</button>
                        <button onclick="setSpeed({lesson['id']}, 0.9)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #fff; cursor: pointer;">0.9x</button>
                        <button onclick="setSpeed({lesson['id']}, 1.0)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #2563eb; color: white; cursor: pointer;">1.0x</button>
                        <button onclick="setSpeed({lesson['id']}, 1.2)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #fff; cursor: pointer;">1.2x</button>
                        <button onclick="setSpeed({lesson['id']}, 1.5)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #fff; cursor: pointer;">1.5x</button>
                        <button onclick="setSpeed({lesson['id']}, 2.0)" style="padding: 3px 8px; border-radius: 6px; border: 1px solid #cbd5e1; background: #fff; cursor: pointer;">2.0x</button>
                        
                        <label style="margin-left: auto; display: flex; align-items: center; gap: 6px; font-weight: 600; font-size: 0.85rem; color: #1e293b; cursor: pointer;">
                            <input type="checkbox" onchange="toggleRepeat({lesson['id']}, this.checked)"> 🔁 Auto Repeat (Lặp bài)
                        </label>
                    </div>
                </div>

                <script>
                    function setSpeed(id, speed) {{
                        var audio = document.getElementById('audio_' + id);
                        if (audio) audio.playbackRate = speed;
                    }}
                    function toggleRepeat(id, isChecked) {{
                        var audio = document.getElementById('audio_' + id);
                        if (audio) audio.loop = isChecked;
                    }}
                </script>
                """
                st.components.v1.html(audio_html, height=115)
            else:
                st.error(
                    f"⚠️ File audio/`{lesson['file']}` chưa có trong thư mục audio local!"
                )

            # Khung hiển thị Script & Dịch song song
            with st.expander("📖 Hiển thị Script & Dịch nghĩa", expanded=False):
                col1, col2 = st.columns(2)

                # Nút Toggle đặt ở trên hai cột để kiểm soát hiển thị Dịch
                show_vi = st.toggle("🌐 Xem Dịch Tiếng Việt", key=f"vi_{lesson['id']}")

                with col1:
                    st.caption("🇺🇸 **Tiếng Anh (Script):**")
                    st.markdown(
                        f"<div class='script-box script-en'>{lesson['en']}</div>",
                        unsafe_allow_html=True,
                    )

                with col2:
                    st.caption("🇻🇳 **Tiếng Việt (Dịch nghĩa):**")
                    if show_vi:
                        st.markdown(
                            f"<div class='script-box script-vi'>{lesson['vi']}</div>",
                            unsafe_allow_html=True,
                        )
                    else:
                        st.info(
                            "Bật công tắc **'Xem Dịch Tiếng Việt'** ở trên để xem bản dịch."
                        )

            st.divider()

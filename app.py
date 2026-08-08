import base64
import os
import streamlit as st

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="English Listening Center",
    page_icon="🎧",
    layout="wide"
)

# Custom CSS canh lề chuẩn cho 2 cột Script & Dịch
st.markdown("""
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
""", unsafe_allow_html=True)

# Header chính
st.markdown("""
<div class="main-header">
    <h1>🎧 English Listening Center</h1>
    <p style="color: #64748b; font-size: 1.1rem;">Ứng dụng ôn luyện 65 bài nghe thông minh</p>
    <div class="author-badge">Author: Phát Phan</div>
</div>
""", unsafe_allow_html=True)

# Hàm mã hóa file audio local thành base64
def get_audio_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# KHAI BÁO DANH SÁCH BÀI HỌC (ĐÃ SỬA LỖI NAMEERROR)
LESSONS = [
    {
        "id": 1, "title": "One | Bought | Buy", "icon": "🍽️", "file": "A1.Q1-5.mp3",
        "en": """Listen to Sue talking to a friend about her new clothes.
Hi Sue, have you been to the shops?
Yes, I had some money for my birthday, so I decided to buy some clothes.
I love those purple jeans.
Yes, I bought them because purple is my favourite colour.
I got a new jacket too.
My old one is too small, so I bought this lovely big one.
It's really great. Did you buy a dress?
I got this one because it was only £9.
That's not expensive.
Then I got a sweater to wear with my jeans.
It's lovely and soft.
That's why I bought it.
Anything else?
A coat.
The long one I have is too big and heavy, but this one is really light.
Did you buy a short white t-shirt like mine?
Well, I bought a long white one.
I'll wear it more often than a short one.""",
        "vi": """Nghe Sue nói chuyện với một người bạn về quần áo mới của cô ấy.
Xin chào Sue, bạn đã đến cửa hàng chưa?
Vâng, tôi có một số tiền cho ngày sinh nhật của mình nên tôi quyết định mua một ít quần áo.
Tôi yêu những chiếc quần jean màu tím đó.
Vâng, tôi mua chúng vì màu tím là màu tôi yêu thích nhất.
Tôi cũng có một chiếc áo khoác mới.
Cái cũ của tôi quá nhỏ nên tôi đã mua cái lớn xinh xắn này.
Nó thực sự tuyệt vời. Bạn đã mua một chiếc váy?
Tôi mua cái này vì nó chỉ có £9.
Điều đó không đắt tiền.
Sau đó tôi có một chiếc áo len để mặc với quần jean của mình.
Nó thật đáng yêu và mềm mại.
Đó là lý do tôi mua nó.
Còn gì nữa không?
Một chiếc áo khoác.
Cái dài tôi có thì quá to và nặng, nhưng cái này thì thực sự nhẹ.
Bạn có mua một chiếc áo phông trắng ngắn như của tôi không?
Vâng, tôi đã mua một cái dài màu trắng.
Tôi sẽ mặc nó thường xuyên hơn là một chiếc ngắn."""
    },
    {
        "id": 2, "title": "See | Going | Then", "icon": "🍔", "file": "A1.Q11-15.mp3",
        "en": """Listen to Rose talking to Steve about her day.
Hi Rose, can you help me with my English homework?
No, Steve. I'm very busy this morning. At 9 o'clock, I'm going to see the doctor.
Well, what are you going to do after that?
I go swimming every day now, just for one hour, so I'm going to do that at 10.
Well, can I meet you at 11?
Sorry, I've got to see my maths teacher then.
And then I suppose you'll go to the library to study.
Not today. At 12, I must meet Bill. I need to talk to him.
So I'll see you at lunchtime, at 1 o'clock.
I'm going to have lunch with Joe then, but you can come too.
No thanks. I'll see you afterwards.
Well, I have an art class at 2, but I can help you after that.
Okay, I'll see you at 3 then.""",
        "vi": """Hãy nghe Rose nói chuyện với Steve về ngày của cô ấy.
Xin chào Rose, bạn có thể giúp tôi làm bài tập tiếng Anh được không?
Không, Steve. Sáng nay tôi rất bận. Lúc 9 giờ tôi sẽ đến gặp bác sĩ.
Này, sau đó bạn định làm gì?
Bây giờ tôi đi bơi mỗi ngày, chỉ trong một giờ, vì vậy tôi sẽ bơi vào lúc 10 giờ.
Vâng, tôi có thể gặp bạn lúc 11 giờ được không?
Xin lỗi, lúc đó tôi phải gặp giáo viên toán của tôi.
Và sau đó tôi cho rằng bạn sẽ đến thư viện để học.
Không phải hôm nay. Lúc 12 tuổi, tôi phải gặp Bill. Tôi cần nói chuyện với anh ấy.
Vậy tôi sẽ gặp bạn vào giờ ăn trưa, lúc 1 giờ.
Vậy tôi sẽ ăn trưa với Joe, nhưng bạn cũng có thể đi cùng.
Không, cảm ơn. Tôi sẽ gặp bạn sau.
À, tôi có lớp nghệ thuật lúc 2 tuổi, nhưng tôi có thể giúp bạn sau lớp đó.
Được rồi, tôi sẽ gặp bạn lúc 3 giờ."""
    }
    # Thêm các bài học tiếp theo vào đây...
]

# Sidebar bộ lọc bài nghe
st.sidebar.header("🔍 Lọc bài nghe")
search_term = st.sidebar.text_input("Tìm kiếm theo tên hoặc từ khóa:", "")

# Vòng lặp hiển thị danh sách bài học
for lesson in LESSONS:
    if search_term.lower() in lesson['title'].lower() or search_term.lower() in str(lesson['id']):
        with st.container():
            st.markdown(f"### Bài {lesson['id']}. {lesson['icon']} {lesson['title']} `{lesson['file']}`")
            
            audio_path = os.path.join("audio", lesson['file'])
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
                st.error(f"⚠️ File audio/`{lesson['file']}` chưa có trong thư mục audio local/repository!")

            # Khung hiển thị Script & Dịch song song
            with st.expander("📖 Hiển thị Script & Dịch nghĩa", expanded=False):
                show_vi = st.toggle("🌐 Xem Dịch Tiếng Việt", key=f"vi_{lesson['id']}")
                col1, col2 = st.columns(2)

                with col1:
                    st.caption("🇺🇸 **Tiếng Anh (Script):**")
                    st.markdown(f"<div class='script-box script-en'>{lesson['en']}</div>", unsafe_allow_html=True)
                
                with col2:
                    st.caption("🇻🇳 **Tiếng Việt (Dịch nghĩa):**")
                    if show_vi:
                        st.markdown(f"<div class='script-box script-vi'>{lesson['vi']}</div>", unsafe_allow_html=True)
                    else:
                        st.info("Bật công tắc **'Xem Dịch Tiếng Việt'** ở trên để xem bản dịch.")
            
            st.divider()

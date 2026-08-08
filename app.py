import base64
import os
import streamlit as st

# 1. Thiết lập cấu hình trang
st.set_page_config(
    page_title="English Listening Center", page_icon="🎧", layout="wide"
)

# 2. Custom CSS canh lề chuẩn cho 2 cột Script & Dịch
st.markdown(
    """
<style>
    .main-header { text-align: center; margin-bottom: 30px; }
    .author-badge { 
        display: inline-block; background-color: #eff6ff; color: #2563eb; 
        font-weight: 700; padding: 6px 16px; border-radius: 9999px; 
        border: 1px solid #dbeafe; margin-top: 5px; 
    }
    
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

# 3. Header chính
st.markdown(
    """
<div class="main-header">
    <h1>🎧 English Listening Center</h1>
    <p style="color: #64748b; font-size: 1.1rem;">Ứng dụng ôn luyện 65 bài nghe thông minh</p>
    <div class="author-badge">Author: Phát Phan</div>
</div>
""",
    unsafe_allow_html=True,
)


# 4. Hàm mã hóa file audio local thành base64
def get_audio_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# 5. DANH SÁCH TOÀN BỘ 65 BÀI HỌC
LESSONS = [
    {
        "id": 1,
        "title": "One | Bought | Buy",
        "icon": "🍽️",
        "file": "A1.Q1-5.mp3",
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
Tôi sẽ mặc nó thường xuyên hơn là một chiếc ngắn.""",
    },
    {
        "id": 2,
        "title": "See | Going | Then",
        "icon": "🍔",
        "file": "A1.Q11-15.mp3",
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
Được rồi, tôi sẽ gặp bạn lúc 3 giờ.""",
    },
    {
        "id": 3,
        "title": "Drive | Driving | Listen",
        "icon": "🎓",
        "file": "A1.Q16-20.mp3",
        "en": """Listen to Peter talking to a friend about learning to drive.
Now listen to the conversation.
Peter, you're learning to drive aren't you?
Do you go to the AA driving school?
Actually it's called the ABC driving school.
Is it expensive?
I want to learn to drive.
It's cost me £140 already.
I've had ten lessons and each one is £14.
Is that for an hour?
Less than that. About three-quarters of an hour.
I see. And is the teacher's car new?
Yes, and it's not a big car so parking's easy.
But it doesn't go very fast.
When are you going to take your driving test?
I failed it last week.
The traffic lights were red, but I didn't see them and I couldn't break in time.
Oh, never mind. You can take the test again.
Tell me about your teacher. Is he friendly?
He's okay. He's quite young and interesting to talk to.
But my father will give me my next lessons. He's cheaper.
Well, good luck.""",
        "vi": """Hãy nghe Peter nói chuyện với một người bạn về việc học lái xe.
Bây giờ hãy nghe cuộc trò chuyện.
Peter, cậu đang học lái xe phải không?
Bạn có đến trường dạy lái xe AA không?
Thật ra nó được gọi là trường dạy lái xe ABC.
Nó có đắt không?
Tôi muốn học lái xe.
Nó đã tốn của tôi 140 bảng rồi.
Tôi đã học 10 bài và mỗi bài có giá 14 bảng.
Có phải trong một giờ không?
Ít hơn thế. Khoảng ba phần tư giờ.
Tôi hiểu rồi. Và xe của thầy có mới không?
Vâng, và nó không phải là một chiếc ô tô lớn nên việc đỗ xe rất dễ dàng.
Nhưng nó không đi rất nhanh.
Khi nào bạn sẽ thi bằng lái xe?
Tôi đã thất bại vào tuần trước.
Đèn giao thông đang đỏ nhưng tôi không nhìn thấy và không kịp vượt qua.
Ồ, đừng bận tâm. Bạn có thể làm bài kiểm tra lại.
Hãy kể cho tôi nghe về giáo viên của bạn. Anh ấy có thân thiện không?
Anh ấy ổn. Anh ấy khá trẻ và thú vị để nói chuyện.
Nhưng cha tôi sẽ cho tôi những bài học tiếp theo. Anh ấy rẻ hơn.
Vâng, chúc may mắn.""",
    },
    {
        "id": 4,
        "title": "His | Look | Patrick",
        "icon": "🍕",
        "file": "A1.Q21-25.mp3",
        "en": """Listen to Patrick talking to his mother about a photo of his old school friends.
How is the party with your old school friends, Patrick?
Great, mother. We've changed a lot since 1990. Look at this photo.
Was Peter there?
Yes. This is him and a sports jacket.
Oh, yes. And his Martin still wear a T-shirt and dirty jeans.
Well, he's a businessman now, so he can't be dirty. But he was wearing jeans.
Look.
Oh, yes. And is this person with the long coat Joanna?
It's like her, isn't it? But Joanna's standing next to Amy and wearing a red sweater.
Is that Amy? I can't believe it. She's so thin.
That black dress doesn't look very good on her.
Hmm, she's been ill. That man in the big hat is a husband, James.
Oh. Isn't that Robert?
No. See the man in the red T-shirt with the blue trousers? That's Robert.
How people change.""",
        "vi": """Hãy nghe Patrick nói chuyện với mẹ về bức ảnh của những người bạn học cũ của anh ấy.
Bữa tiệc với bạn học cũ của cậu thế nào, Patrick?
Tuyệt quá mẹ ơi. Chúng tôi đã thay đổi rất nhiều kể từ năm 1990. Hãy nhìn bức ảnh này.
Peter có ở đó không?
Đúng. Đây là anh ấy và một chiếc áo khoác thể thao.
Ồ, vâng. Và chiếc Martin của anh ấy vẫn mặc áo phông và quần jean bẩn.
Thôi, bây giờ anh ấy là doanh nhân nên không thể bẩn được. Nhưng anh ấy lại mặc quần jean.
Nhìn.
Ồ, vâng. Và người mặc áo khoác dài này có phải là Joanna không?
Nó giống cô ấy phải không? Nhưng Joanna đang đứng cạnh Amy và mặc chiếc áo len màu đỏ.
Đó có phải là Amy không? Tôi không thể tin được. Cô ấy gầy quá.
Chiếc váy đen đó trông không đẹp lắm với cô ấy.
Hmm, cô ấy bị ốm. Người đàn ông đội chiếc mũ lớn đó là một người chồng, James.
Ồ. Đó không phải là Robert sao?
Không. Bạn có thấy người đàn ông mặc áo phông đỏ quần xanh không? Đó là Robert.
Con người thay đổi thế nào.""",
    },
    {
        "id": 5,
        "title": "School | Now | Well",
        "icon": "✈️",
        "file": "A1.Q26-30.mp3",
        "en": """Listen to Jenny asking Mark about school holiday activities.
Now, listen to the conversation.
Hello, Jenny. What are you doing here?
Mark, hello. This is my daughter, Sarah.
It's the school holiday, so we're shopping now.
We're not sure what to do after that.
Well, there's a show for children this afternoon in the library where I work.
Oh, what time is the show?
It starts at two and finishes at 3.30.
It's only quarter past one now. What about that?
How much is a ticket?
Well, it's £1.50 for adults and £75 for children.
Programs are £25.
And does your library do a reading course in the holidays?
Yes. And if children under 10, like Sarah, read four books in six weeks, we give them something to take home.
Oh, like a book?
Well, this year it's a pen, but sometimes it's a book or a school bag.
Meet me after the show and I'll tell you what to do.
Thanks. See you later then.""",
        "vi": """Nghe Jenny hỏi Mark về các hoạt động trong kỳ nghỉ ở trường.
Bây giờ, hãy lắng nghe cuộc trò chuyện.
Xin chào, Jenny. Bạn đang làm gì ở đây?
Mark, xin chào. Đây là con gái tôi, Sarah.
Hôm nay là ngày nghỉ học nên bây giờ chúng tôi đang đi mua sắm.
Chúng tôi không chắc chắn phải làm gì sau đó.
À, chiều nay có buổi biểu diễn dành cho trẻ em ở thư viện nơi tôi làm việc.
Ồ, chương trình diễn ra lúc mấy giờ?
Nó bắt đầu lúc hai giờ và kết thúc lúc 3 giờ 30.
Bây giờ mới là một giờ mười lăm. Thế còn chuyện đó thì sao?
Một vé bao nhiêu tiền?
Vâng, đó là £1,50 cho người lớn và £75 cho trẻ em.
Các chương trình có giá £25.
Và thư viện của bạn có tổ chức khóa đọc sách vào dịp nghỉ lễ không?
Đúng. Và nếu trẻ em dưới 10 tuổi, như Sarah, đọc bốn cuốn sách trong sáu tuần, chúng tôi sẽ cho chúng thứ gì đó để mang về nhà.
Ồ, giống như một cuốn sách?
À, năm nay là một cây bút, nhưng đôi khi lại là một cuốn sách hoặc một cặp sách.
Gặp tôi sau buổi biểu diễn và tôi sẽ cho bạn biết phải làm gì.
Cảm ơn. Hẹn gặp lại sau nhé.""",
    },
    {
        "id": 6,
        "title": "Concert | London | Some",
        "icon": "🛫",
        "file": "A1.Q31-35.mp3",
        "en": """You will hear some information about a pop concert.
You are listening to Radio South.
Here is some information about a pop concert.
The group Red River will come to London soon.
They will be in London from 28 October to 2 November.
After that they will be in Oxford from 4 November until 9.
It's are quite expensive.
They cost 37 pounds each, but half of that money will go to a children's hospital.
Tickets will sell quickly for this famous band so book early.
To book a ticket for a London concert, telephone 283 0065 between 10am and 10pm.
Have a credit card number ready?
The London concerts will be in South Bank Hall.
It's very easy to find.
The best way to get there is to take the train.
The concert hall is in Trinity Street.
That's T-R-I-N-I-T-Y Street.
See you there.
For Classical Music Lovers?""",
        "vi": """Bạn sẽ nghe một số thông tin về một buổi hòa nhạc pop.
Bạn đang nghe Đài phát thanh miền Nam.
Dưới đây là một số thông tin về một buổi hòa nhạc pop.
Nhóm Red River sẽ sớm đến London.
Họ sẽ ở London từ ngày 28 tháng 10 đến ngày 2 tháng 11.
Sau đó họ sẽ ở Oxford từ ngày 4 tháng 11 đến ngày 9 tháng 11.
Nó khá đắt.
Mỗi chiếc có giá 37 bảng, nhưng một nửa số tiền đó sẽ được chuyển đến bệnh viện nhi.
Vé của ban nhạc nổi tiếng này sẽ được bán rất nhanh nên hãy đặt vé sớm.
Để đặt vé cho buổi hòa nhạc ở London, hãy gọi số 283 0065 trong khoảng thời gian từ 10 giờ sáng đến 10 giờ tối.
Bạn đã có sẵn số thẻ tín dụng chưa?
Buổi hòa nhạc ở London sẽ diễn ra ở South Bank Hall.
Nó rất dễ tìm thấy.
Cách tốt nhất để đến đó là đi tàu.
Phòng hòa nhạc nằm ở phố Trinity.
Đó là đường T-R-I-N-I-T-Y.
Hẹn gặp bạn ở đó.
Dành cho những người yêu thích âm nhạc cổ điển?""",
    },
    {
        "id": 7,
        "title": "Health | Centre | Tomorrow",
        "icon": "🛒",
        "file": "A1.Q36-40.mp3",
        "en": """You will hear some information about a health centre.
This is the Mill House Health Centre.
The health centre is closed until 8 o'clock tomorrow morning,
but here is some important information.
To make an appointment with one of the doctors, you can phone us tomorrow.
The number is 793-220.
The health centre is always very busy early in the morning,
so please do not phone before 830.
If you want to get medicine, Padley's chemist shop,
that's P-A-D-L-E-Y-S,
is open until 10pm every evening this week, including Sundays.
Take the 77 bus to the high street,
the stop is right outside the shop.
If you need to see a doctor now,
please go to the accident department at University Hospital.
They're open 24 hours a day for accidents and emergencies.
Thank you for calling the Mill House Health Centre this evening.
Our doctors and nurses will be pleased to answer any more of your questions tomorrow.""",
        "vi": """Bạn sẽ nghe một số thông tin về một trung tâm y tế.
Đây là Trung tâm Y tế Mill House.
Trung tâm y tế đóng cửa đến 8 giờ sáng mai,
nhưng đây là một số thông tin quan trọng.
Để đặt lịch hẹn với một trong các bác sĩ, bạn có thể gọi điện cho chúng tôi vào ngày mai.
Số là 793-220.
Trung tâm y tế luôn rất đông đúc vào mỗi buổi sáng sớm,
vì vậy vui lòng không gọi điện trước 8 giờ 30.
Nếu bạn muốn mua thuốc, hãy tới hiệu thuốc Padley,
đó là P-A-D-L-E-Y-S,
mở cửa đến 22h mỗi tối trong tuần này, kể cả Chủ Nhật.
Đi xe buýt 77 tới đường cao tốc,
điểm dừng ở ngay bên ngoài cửa hàng.
Nếu bạn cần gặp bác sĩ bây giờ,
hãy đến khoa tai nạn của Bệnh viện Đại học.
Họ mở cửa 24 giờ một ngày khi có tai nạn và trường hợp khẩn cấp.
Cảm ơn bạn đã gọi đến Trung tâm Y tế Mill House tối nay.
Các bác sĩ và y tá của chúng tôi sẽ sẵn lòng trả lời thêm bất kỳ câu hỏi nào của bạn vào ngày mai.""",
    },
    {
        "id": 8,
        "title": "Sarah | Here | Hotel",
        "icon": "🍜",
        "file": "A1.Q41-45.mp3",
        "en": """Listen to Sarah, talking to a friend about her holiday photographs.
I've got some photos of my holiday in Spain here.
Did you go with your family, Sarah?
Yes. This is my mother walking in the mountains.
What lovely trees.
And this is my sister Caroline Swimming.
She preferred swimming here to the hotel pool.
The sea looks very blue.
And who's this standing outside a castle?
Jack. But it's not a castle. It's a cathedral.
It's one of the oldest in Spain.
And is this you, Sarah, buying bananas in a market?
Yes. That wasn't far from our hotel.
The fruit was really cheap there.
And here's Peter eating.
Is he in the garden of your hotel?
Actually, it's a restaurant near the cathedral. We often went there.
What's your father doing with the cassette recorder in this photo?
Oh, he loves history.
He's in a museum here listening to information.
That was his favorite day, because we also visited a castle in the morning.
They're great photos, Sarah.""",
        "vi": """Hãy nghe Sarah nói chuyện với một người bạn về những bức ảnh trong kỳ nghỉ của cô ấy.
Tôi có một số bức ảnh về kỳ nghỉ của tôi ở Tây Ban Nha ở đây.
Bạn có đi cùng gia đình không, Sarah?
Đúng. Đây là mẹ tôi đang đi dạo trên núi.
Những cái cây đáng yêu làm sao.
Và đây là em gái tôi Caroline Bơi lội.
Cô thích bơi ở đây hơn hồ bơi của khách sạn.
Biển trông rất xanh.
Và ai đang đứng bên ngoài lâu đài?
Jack. Nhưng nó không phải là một lâu đài. Đó là một nhà thờ.
Đây là một trong những lâu đời nhất ở Tây Ban Nha.
Và đây có phải là bạn không, Sarah, đang mua chuối ở chợ?
Đúng. Chỗ đó không xa khách sạn của chúng tôi.
Trái cây ở đó thực sự rẻ.
Và đây là Peter đang ăn.
Anh ấy có ở trong vườn khách sạn của bạn không?
Thật ra, đó là một nhà hàng gần nhà thờ. Chúng tôi thường đến đó.
Bố bạn đang làm gì với chiếc máy ghi âm trong bức ảnh này?
Ồ, anh ấy yêu lịch sử.
Anh ấy đang ở trong viện bảo tàng để nghe thông tin.
Đó là ngày yêu thích của anh ấy, vì chúng tôi cũng đã đến thăm một lâu đài vào buổi sáng.
Đó là những bức ảnh tuyệt vời, Sarah.""",
    },
    {
        "id": 9,
        "title": "Don | Then | Listen",
        "icon": "☕",
        "file": "A1.Q46-50.mp3",
        "en": """Listen to Sue talking to her friend Jim about the new sports centre.
Now listen to the conversation.
Have you been to the new sports centre, Jim?
Yes, Sue. It's not cheap, but it's big and light.
Does bus 18 go there?
That's right. It takes 15 minutes.
Don't get bus 25, because you have to walk a long way.
I like doing sport early in the morning. Is it open at 7?
Yes. You can go there from 6, except on Sundays. Then it doesn't open until 9.
The swimming pool has good hot showers. You have to bring your own towel, but you can get soap there.
They don't make you wear a swimming hat.
Do they sell things to eat there?
Only sandwiches. They don't sell drinks.
I usually take some fruit.
I'd love to go with you next week. How about Wednesday?
Well, I work until late on Wednesday. I'm free on Saturday, but it's too busy then.
It'll have to be Thursday.
Okay. See you then.""",
        "vi": """Hãy nghe Sue nói chuyện với bạn của cô ấy là Jim về trung tâm thể thao mới.
Bây giờ hãy nghe cuộc trò chuyện.
Bạn đã đến trung tâm thể thao mới chưa, Jim?
Vâng, Sue. Nó không rẻ, nhưng nó to và nhẹ.
Xe buýt số 18 có đến đó không?
Đúng vậy. Phải mất 15 phút.
Đừng bắt xe buýt số 25 vì bạn phải đi bộ một quãng đường dài.
Tôi thích chơi thể thao vào buổi sáng sớm. Nó có mở cửa lúc 7 giờ không?
Đúng. Bạn có thể đến đó từ 6 giờ, trừ Chủ Nhật. Sau đó, nó không mở cho đến 9.
Hồ bơi có vòi sen nước nóng tốt. Bạn phải mang theo khăn riêng, nhưng bạn có thể lấy xà phòng ở đó.
Họ không bắt bạn phải đội mũ bơi.
Ở đó có bán đồ ăn không?
Chỉ có bánh mì sandwich. Họ không bán đồ uống.
Tôi thường ăn một ít trái cây.
Tôi rất muốn đi cùng bạn vào tuần tới. Thế còn thứ Tư thì sao?
À, tôi làm việc đến tận khuya thứ Tư. Thứ Bảy tôi rảnh, nhưng lúc đó bận quá.
Sẽ phải là thứ Năm.
Được rồi. Hẹn gặp lại sau.""",
    },
    {
        "id": 10,
        "title": "Centre | Get | Shopping",
        "icon": "🛬",
        "file": "A1.Q56-60.mp3",
        "en": """Listen to Anne, asking her friend about going to a shopping centre.
Now listen to the conversation.
Anne, have you been to that new shopping centre?
The Forest Centre.
No, I mean Queens, the new one near the river.
Oh, I've seen the advertisement, it's got the largest cafe and bookshop in the country.
It will have only the clothes shops are open this month.
Well, that's okay, but it's at least 30 kilometres away and I haven't got a car.
Well, there is a coach once a week.
It's there, I can get that if it's not on Saturday, I have to work then.
It goes on Tuesday, but it's best to get your ticket on Monday.
Is the ticket expensive?
£10.80 for adults, £2.50 for children and only £5.60 for students like you.
Not bad.
Does it go from the bus station?
Yes, and it stops in Market Square and outside the museum in Broad Street.
Oh, good, I'll get it there.
Broad Street is really near my house.
Does it leave early?
20 past nine.
And you get to the shopping centre 40 minutes later at 10 o'clock.
Great!""",
        "vi": """Hãy nghe Anne hỏi bạn cô ấy về việc đi đến trung tâm mua sắm.
Bây giờ hãy nghe cuộc trò chuyện.
Anne, bạn đã đến trung tâm mua sắm mới đó chưa?
Trung tâm Rừng.
Không, ý tôi là Queens, cái mới gần sông.
Ồ, tôi đã xem quảng cáo, ở đó có quán cà phê và hiệu sách lớn nhất cả nước.
Nó sẽ chỉ có các cửa hàng quần áo được mở trong tháng này.
Không sao đâu, nhưng phải xa ít nhất 30km mà tôi lại không có xe.
Vâng, có một huấn luyện viên mỗi tuần một lần.
Nó ở đó, tôi có thể lấy được nếu không phải thứ bảy thì tôi phải làm việc.
Nó diễn ra vào thứ Ba, nhưng tốt nhất bạn nên lấy vé vào thứ Hai.
Vé có đắt không?
£10,80 cho người lớn, £2,50 cho trẻ em và chỉ £5,60 cho sinh viên như bạn.
Không tệ.
Nó có đi từ bến xe buýt không?
Vâng, và nó dừng ở Quảng trường Chợ và bên ngoài bảo tàng ở Phố Broad.
Ồ, tốt, tôi sẽ lấy nó ở đó.
Phố Broad thực sự rất gần nhà tôi.
Nó có rời đi sớm không?
9 giờ 20.
Và bạn đến trung tâm mua sắm 40 phút sau lúc 10 giờ.
Tuyệt vời!""",
    },
    {
        "id": 11,
        "title": "One | Card | Jan",
        "icon": "🚁",
        "file": "A1.Q6-10.mp3",
        "en": """Listen to Jan talking to Steve about getting a student travel card.
Hi Steve.
Hi Jan.
I'm going to go to London on the train.
Come with me.
But it's cheaper by bus.
I've got a student travel card.
You can get cheap train tickets with it.
Oh that sounds good.
How much does it cost?
A card for six months is 16 pounds.
So how do I get one?
You need some photographs, one for the card and one for the form.
Oh.
There's a photo machine in the post office.
It gives you four photos for three pounds.
So does the one in the library.
But I went to a photographer shop.
It was cheaper.
I don't have to show my passport or my driving license, do I?
That's right Jan.
You only need a letter from your college.
I'll ask my teacher for one.
And then you take everything to the tourist office by the travel agents.
Great.
Next time you go to London, I'll come too.""",
        "vi": """Hãy nghe Jan nói chuyện với Steve về việc lấy thẻ du lịch dành cho sinh viên.
Chào Steve.
Chào Jan.
Tôi sẽ đi London bằng tàu hỏa.
Hãy đi với tôi.
Nhưng nó rẻ hơn bằng xe buýt.
Tôi có thẻ du lịch sinh viên.
Bạn có thể nhận được vé tàu giá rẻ với nó.
Ồ, điều đó nghe có vẻ hay đấy.
Nó có giá bao nhiêu?
Một thẻ dùng trong sáu tháng là 16 pound.
Vậy làm thế nào để tôi có được một cái?
Bạn cần một số bức ảnh, một tấm cho thẻ và một tấm cho mẫu đơn.
Ồ.
Có một máy chụp ảnh ở bưu điện.
Nó cung cấp cho bạn bốn bức ảnh với giá ba bảng Anh.
Cái trong thư viện cũng vậy.
Nhưng tôi đã đến một cửa hàng nhiếp ảnh gia.
Nó rẻ hơn.
Tôi không cần phải xuất trình hộ chiếu hoặc bằng lái xe, phải không?
Đúng rồi Jan.
Bạn chỉ cần một lá thư từ trường đại học của bạn.
Tôi sẽ xin giáo viên của tôi một cái.
Sau đó bạn sẽ được các đại lý du lịch mang mọi thứ đến văn phòng du lịch.
Tuyệt vời.
Lần tới khi bạn tới London, tôi cũng sẽ đi.""",
    },
    {
        "id": 12,
        "title": "Too | Sarah | Sports",
        "icon": "🍎",
        "file": "A1.Q71-75.mp3",
        "en": """Listen to Sarah talking to a friend about a sports centre.
I like your new t-shirt, Sarah.
The colours are nice, but the problem is it's too big.
I got it from the shop at the sports centre.
I went swimming there because it was a hot day, but it was too noisy for me.
There were a lot of people in the pool.
So was it difficult to find a space in the car park there?
Yes, it's not big enough.
Did you go to the cafe?
Yes, for a cold drink, but I didn't stay.
The tables and floor weren't clean.
But I hear they have a good football club there.
That's right.
My brother wanted to go, but it starts too late in the evening for him.
It's a pity because it's not an expensive club.
Can you learn tennis there?
I called about lessons, but they cost too much.
I'll teach you tennis, but not today.
It's too hot.
Let's go for a cold swim in the river.""",
        "vi": """Nghe Sarah nói chuyện với một người bạn về một trung tâm thể thao.
Tôi thích chiếc áo phông mới của bạn, Sarah.
Màu sắc đẹp, nhưng vấn đề là nó quá lớn.
Tôi mua nó từ cửa hàng ở trung tâm thể thao.
Tôi đến đó bơi vì trời nắng nóng nhưng lại quá ồn ào đối với tôi.
Có rất nhiều người trong hồ bơi.
Vậy tìm chỗ đậu xe ở đó có khó không?
Vâng, nó không đủ lớn.
Bạn đã đến quán cà phê chưa?
Vâng, để uống nước lạnh, nhưng tôi đã không ở lại.
Bàn và sàn không sạch sẽ.
Nhưng tôi nghe nói ở đó có một câu lạc bộ bóng đá rất tốt.
Đúng vậy.
Anh trai tôi muốn đi, nhưng trời đã quá khuya đối với anh ấy.
Thật đáng tiếc vì đây không phải là một câu lạc bộ đắt tiền.
Bạn có thể học quần vợt ở đó không?
Tôi đã gọi điện về các bài học nhưng chúng đắt quá.
Tôi sẽ dạy bạn quần vợt, nhưng không phải hôm nay.
Trời nóng quá.
Chúng ta hãy đi bơi lạnh trên sông.""",
    },
    {
        "id": 13,
        "title": "Course | College | Pounds",
        "icon": "🍩",
        "file": "A1.Q76-80.mp3",
        "en": """Listen to Philip, talking to a friend about his photography course.
Now listen to the conversation.
Hello Philip, are you doing a photography course?
Yes, there wasn't one at my college, Park College, so I go to City College in South Road.
Are you classes in the evening?
Yes, I finish at Park College at quarter past five and get home about six.
The lessons start at quarter to seven. I have just enough time to eat.
How much are they?
My ten week course is usually 95 pounds, but it costs me 75 pounds because I'm a student.
There's also a five week course for 55 pounds.
Is it a good course?
Yes, great.
The cameras are rather old, but my photos are much better now, so I'm really pleased.
I'll never be a famous photographer, though.
I think taking photographs is difficult.
Well, we did animals first, and they're certainly not easy.
But then we took pictures of trees, and that wasn't difficult.
We'll photograph children next.
And after the course?
There aren't many jobs for photographers. It'll be my hobby.
I can use my father's camera, but I'll have to buy a lot of film.""",
        "vi": """Hãy nghe Philip nói chuyện với một người bạn về khóa học nhiếp ảnh của anh ấy.
Bây giờ hãy nghe cuộc trò chuyện.
Xin chào Philip, bạn đang tham gia một khóa học nhiếp ảnh phải không?
Vâng, không có trường nào ở trường đại học của tôi, Park College, vì vậy tôi vào City College ở South Road.
Bạn có lớp học vào buổi tối không?
Vâng, tôi học xong ở Park College lúc 5 giờ 15 và về nhà vào khoảng 6 giờ.
Các bài học bắt đầu lúc bảy giờ kém mười lăm. Tôi chỉ có đủ thời gian để ăn.
Chúng giá bao nhiêu?
Khóa học 10 tuần của tôi thường có giá 95 bảng, nhưng tôi phải trả 75 bảng vì tôi là sinh viên.
Ngoài ra còn có một khóa học 5 tuần với giá 55 pound.
Đây có phải là một khóa học tốt?
Vâng, tuyệt vời.
Máy ảnh khá cũ nhưng ảnh của tôi bây giờ đẹp hơn nhiều nên tôi rất hài lòng.
Tuy nhiên, tôi sẽ không bao giờ trở thành một nhiếp ảnh gia nổi tiếng.
Tôi nghĩ việc chụp ảnh là khó khăn.
Chà, chúng tôi đã làm động vật trước tiên và chúng chắc chắn không hề dễ dàng.
Nhưng sau đó chúng tôi chụp ảnh cây cối và việc đó không khó khăn gì.
Tiếp theo chúng ta sẽ chụp ảnh trẻ em.
Và sau khóa học?
Không có nhiều việc làm cho nhiếp ảnh gia. Nó sẽ là sở thích của tôi.
Tôi có thể sử dụng máy ảnh của bố tôi nhưng tôi sẽ phải mua rất nhiều phim.""",
    },
    {
        "id": 14,
        "title": "Restaurant | Lena | Our",
        "icon": "🍣",
        "file": "A1.Q81-85.mp3",
        "en": """Listen to Lena talking to a friend about some restaurants.
We've got to choose a restaurant for our class party next Saturday, Lena.
What about the Rose Garden?
It'll be too cold because all the tables are outside.
I suppose Carla's cafe is still closed.
It's open again now, but it's not big enough for all of our class.
And what do you think about pizza place?
The food's good, but they turn the lights so low it's impossible to read the menu.
What about the curry house?
The waiters are really friendly and everyone likes Indian food.
I phoned them yesterday.
They're fully booked on Saturday, so there won't be any tables free.
Oh dear.
I've just been to that new fish restaurant, Captain Krab.
The music was so loud it was impossible to have a conversation.
We'll want to talk, so that's no good.
I suppose there's the Colton Hotel.
Even a snack there costs a lot of money.
We need a cheaper restaurant.
Let's look in the newspaper.""",
        "vi": """Nghe Lena nói chuyện với một người bạn về một số nhà hàng.
Chúng ta phải chọn một nhà hàng cho bữa tiệc của lớp vào thứ Bảy tới, Lena.
Còn Vườn Hồng thì sao?
Trời sẽ rất lạnh vì tất cả các bàn đều ở bên ngoài.
Tôi cho rằng quán cà phê của Carla vẫn đóng cửa.
Bây giờ nó đã mở cửa trở lại nhưng không đủ chỗ cho cả lớp chúng tôi.
Và bạn nghĩ gì về nơi bán pizza?
Thức ăn ngon, nhưng họ tắt đèn quá thấp nên không thể đọc được thực đơn.
Còn nhà cà ri thì sao?
Những người phục vụ thực sự thân thiện và mọi người đều thích đồ ăn Ấn Độ.
Tôi đã gọi điện cho họ ngày hôm qua.
Chúng đã được đặt kín chỗ vào thứ Bảy nên sẽ không còn bàn nào trống.
Ôi trời ơi.
Tôi vừa đến nhà hàng cá mới đó, Thuyền trưởng Krab.
Âm nhạc quá to đến nỗi không thể có một cuộc trò chuyện.
Chúng ta sẽ muốn nói chuyện, nên điều đó không tốt chút nào.
Tôi cho là ở đó có khách sạn Colton.
Ngay cả một bữa ăn nhẹ ở đó cũng tốn rất nhiều tiền.
Chúng ta cần một nhà hàng rẻ hơn.
Chúng ta hãy nhìn vào tờ báo.""",
    },
    {
        "id": 15,
        "title": "Nick | Band | Helen",
        "icon": "🍦",
        "file": "A1.Q86-90.mp3",
        "en": """Listen to Helen talking to her friend Sam about being in a rock band.
Now listen to the conversation.
Sam, you know I sing in Nick's band.
He plays drums, doesn't he, Helen?
Yes. Well, we need another guitar player. How about you?
Sure. Nick wants to hear you play first. Are you free on Wednesday?
Sorry. How about the next day or Friday?
Let's say Thursday. Nick's busy on Fridays.
Fine. Where and what time?
Come to my flat at 730 and we can walk to Nick's.
The band uses his dad's garage because his bedroom's too small.
Should I bring anything? Food, music?
Nick's mum makes a sandwiches and I always bring CDs.
A warm sweat is a good idea because it gets cold.
Okay. When's the band's next concert? Aren't you playing at your brother's 18th birthday party?
Yes. And the college has booked us for the Saturday before that.
We want to play at the Starlight Club but they're fully booked at the moment.
Do you get paid for singing, Helen? Of course.
The band gets £110 a night and we each have £25.
Nick keeps £10 for things like advertisements. Great.""",
        "vi": """Hãy nghe Helen nói chuyện với bạn cô ấy là Sam về việc tham gia một ban nhạc rock.
Bây giờ hãy nghe cuộc trò chuyện.
Sam, bạn biết đấy, tôi hát trong ban nhạc của Nick.
Anh ấy chơi trống phải không Helen?
Đúng. Chà, chúng ta cần một người chơi ghi-ta khác. Còn bạn thì sao?
Chắc chắn. Nick muốn nghe bạn chơi đàn trước. Bạn có rảnh vào thứ Tư không?
Lấy làm tiếc. Thế còn ngày hôm sau hoặc thứ Sáu thì sao?
Hãy nói thứ năm. Nick bận vào thứ Sáu.
Khỏe. Ở đâu và mấy giờ?
Hãy đến căn hộ của tôi lúc 7h30 và chúng ta có thể đi bộ đến chỗ Nick.
Ban nhạc sử dụng gara của bố anh vì phòng ngủ của ông quá nhỏ.
Tôi có nên mang theo gì không? Thức ăn, âm nhạc?
Mẹ của Nick làm bánh sandwich và tôi luôn mang theo đĩa CD.
Đổ mồ hôi ấm là một ý tưởng tốt vì trời sẽ lạnh.
Được rồi. Buổi hòa nhạc tiếp theo của ban nhạc diễn ra khi nào? Không phải bạn đang chơi ở bữa tiệc sinh nhật lần thứ 18 của anh trai mình sao?
Đúng. Và trường đại học đã đặt chỗ cho chúng tôi vào thứ Bảy trước đó.
Chúng tôi muốn chơi ở Starlight Club nhưng hiện tại họ đã kín chỗ.
Cô có được trả tiền khi hát không, Helen? Tất nhiên rồi.
Ban nhạc nhận được 110 bảng một đêm và mỗi người chúng tôi có 25 bảng.
Nick giữ lại £10 cho những thứ như quảng cáo. Tuyệt vời.""",
    },
    {
        "id": 16,
        "title": "Her | She | Did",
        "icon": "🥂",
        "file": "A1.Q91-95.mp3",
        "en": """Listen to Amy, telling her father about her shopping trip.
Did you spend all your money, Amy?
No, Dad, but we all bought something.
Look, I found the video I wanted.
Great!
We spent hours in the department store.
Alison wants to take all her shoes on holiday
and her suitcase is too small.
She bought a new one, but it took her ages.
Then what did you do?
We went with Helen to look at mobile phones.
Her parents are getting her one for her birthday.
So she bought a magazine that had information about all the different kinds to show them.
That's a good idea.
Did Lucy find a present for her mum's birthday?
Yes, she looked at some beautiful shoes, but they were too expensive.
But I think her mum will like the sweater she bought.
Oh, good. What did Carrie buy?
A picture of our favourite band playing it a concert.
Is that the band you saw with Joe?
Yes, she got their new CD today.
The music magazines say it's excellent.
You must all be tired.""",
        "vi": """Hãy nghe Amy kể cho bố cô ấy nghe về chuyến đi mua sắm của cô ấy.
Bạn đã tiêu hết tiền của mình chưa, Amy?
Không, bố, nhưng tất cả chúng ta đều đã mua thứ gì đó.
Hãy nhìn xem, tôi đã tìm thấy video tôi muốn.
Tuyệt vời!
Chúng tôi đã dành hàng giờ trong cửa hàng bách hóa.
Alison muốn mang hết giày đi nghỉ
và vali của cô ấy quá nhỏ.
Cô ấy đã mua một cái mới, nhưng việc đó mất rất nhiều thời gian.
Sau đó bạn đã làm gì?
Chúng tôi cùng Helen đi xem điện thoại di động.
Cha mẹ cô ấy đang tặng cô ấy một chiếc vào ngày sinh nhật của cô ấy.
Vì vậy cô ấy đã mua một tạp chí có thông tin về tất cả các loại khác nhau để cho họ xem.
Đó là một ý tưởng tốt.
Lucy đã tìm được quà cho ngày sinh nhật của mẹ cô ấy chưa?
Vâng, cô ấy đã xem một số đôi giày đẹp, nhưng chúng quá đắt.
Nhưng tôi nghĩ mẹ cô ấy sẽ thích chiếc áo len cô ấy mua.
Ồ, tốt. Carrie đã mua gì?
Hình ảnh ban nhạc yêu thích của chúng tôi biểu diễn trong buổi hòa nhạc.
Đó có phải là ban nhạc bạn đã xem cùng với Joe không?
Vâng, hôm nay cô ấy đã nhận được CD mới của họ.
Các tạp chí âm nhạc đều nói nó rất xuất sắc.
Chắc hẳn các bạn đều mệt mỏi rồi.""",
    },
    {
        "id": 17,
        "title": "Flat | Listen | Jamie",
        "icon": "🏨",
        "file": "A1.Q96-100.mp3",
        "en": """Listen to Jamie talking to his mother about a flat.
Now listen to the conversation.
Hi mom, I've decided to move from my room at the university and into a flat with some friends.
Is the flat near the university Jamie?
About 20 minutes by bicycle and there are buses every half hour.
But I'll walk through the park and have breakfast at a cafe there with my friends.
Will the flat be quiet so you can study?
There's a shoe shop downstairs, but it's never busy and there's not much traffic.
Is it expensive?
200 pounds a week.
But there are five of us, so that's 40 pounds each, which isn't bad.
Good!
Does the flat have a nice kitchen?
Well, the fridge is old and the cook is a bit small, but that doesn't matter.
We can't cook.
Oh, can I still use your washing machine, Mum?
Because there isn't one there.
Of course. When will you move?
On Saturday.
If you can wait until the next day, Dad and I will help you so you're ready for classes on Monday.
Okay. Thanks, Mum.""",
        "vi": """Hãy nghe Jamie nói chuyện với mẹ anh ấy về căn hộ.
Bây giờ hãy nghe cuộc trò chuyện.
Chào mẹ, con quyết định chuyển từ phòng ở trường đại học đến sống trong căn hộ với một số người bạn.
Căn hộ có gần trường đại học Jamie không?
Khoảng 20 phút đi xe đạp và cứ nửa giờ lại có xe buýt.
Nhưng tôi sẽ đi bộ qua công viên và ăn sáng tại một quán cà phê ở đó với bạn bè.
Căn hộ có yên tĩnh để bạn có thể học không?
Có một cửa hàng giày ở tầng dưới nhưng nó không bao giờ đông khách và cũng không có nhiều người qua lại.
Nó có đắt không?
200 bảng một tuần.
Nhưng chúng tôi có năm người, vậy nên mỗi người nặng 40 pound, không tệ.
Tốt!
Căn hộ có nhà bếp đẹp không?
À, tủ lạnh đã cũ và đầu bếp hơi nhỏ, nhưng điều đó không thành vấn đề.
Chúng tôi không thể nấu ăn.
Ồ, con vẫn dùng máy giặt của mẹ được chứ mẹ?
Bởi vì không có ai ở đó cả.
Tất nhiên rồi. Khi nào bạn sẽ di chuyển?
Vào thứ bảy.
Nếu con có thể đợi đến ngày hôm sau, bố và mẹ sẽ giúp con sẵn sàng cho lớp học vào thứ Hai.
Được rồi. Cảm ơn mẹ.""",
    },
    {
        "id": 18,
        "title": "Tonight | Going | Birthday",
        "icon": "🚀",
        "file": "Bo tro 1 PART 1.mp3",
        "en": """Now look at the instructions for part 1.
1. Where will the man and woman meet?
I'll see you outside the cinema at 6 o'clock.
Why can't you meet me at the station? Or better still the cafe?
We're going to eat there before the film aren't we?
Yes, but we need to be at the cinema at 6 to buy the tickets.
Then we can go to the cafe.
Oh, okay.
Now listen again.
I'll see you outside the cinema at 6 o'clock.
Why can't you meet me at the station? Or better still the cafe?
We're going to eat there before the film aren't we?
Yes, but we need to be at the cinema at 6 to buy the tickets.
Then we can go to the cafe.
Oh, okay.
2. Watch the date of Emma's birthday party.
Are you going to Emma's 20th birthday party in June?
Yes, I am, but it's in July actually.
Oh, yes, of course. The 21st, isn't it?
That's right. Her birthday is the day after mine.
That's how I remember it.
Now listen again.
Are you going to Emma's 20th birthday party in June?
Yes, I am, but it's in July actually.
Oh, yes, of course. The 21st, isn't it?
That's right. Her birthday is the day after mine.
That's how I remember it.
3. Where is Nora's watch?
Have you seen my watch, Mum? I left it on the bookshelf.
I think it's in the kitchen, Nora, on the table.
That's your watch, Mum.
Oh, then I'm wearing yours.
Sorry, I thought it was mine.
4. How much is a ticket for tonight?
It is a ticket for tonight.
The ticket for tonight is a ticket for tonight.
I am, oh, thank you.
I'm sorry. She's taking the take again.
She and Vanessa, who asked me to go party nap.
4. How much is a ticket for tonight's match?
Are you going to the basketball match tonight?
How much are the tickets?
Most weeks they're £6, but it's a special price tonight.
£3.50, so do come.
Right. I've got £10 here, so that's okay.
Ka, 5.
Which is the boys brother?
Look, there's my brother over there talking to his friends.
Oh, is he the one with dark hair?
My brother's got blonde hair.
Oh yes, and he's got the same glasses as you.
He looks nice.
Now listen again.
Look, there's my brother over there talking to his friends.
Oh, is he the one with dark hair?
My brother's got blonde hair.
Oh yes, and he's got the same glasses as you.
He looks nice.
This is the end of part one.""",
        "vi": """Bây giờ hãy xem hướng dẫn cho phần 1.
1. Người đàn ông và người phụ nữ sẽ gặp nhau ở đâu?
Tôi sẽ gặp bạn ở ngoài rạp chiếu phim lúc 6 giờ.
Tại sao bạn không thể gặp tôi ở nhà ga? Hay tốt hơn vẫn là quán cà phê?
Chúng ta sẽ ăn ở đó trước khi xem phim phải không?
Đúng, nhưng chúng ta cần có mặt ở rạp chiếu phim lúc 6 giờ để mua vé.
Sau đó chúng ta có thể đi đến quán cà phê.
Ồ, được rồi.
Bây giờ hãy nghe lại.
Tôi sẽ gặp bạn ở ngoài rạp chiếu phim lúc 6 giờ.
Tại sao bạn không thể gặp tôi ở nhà ga? Hay tốt hơn vẫn là quán cà phê?
Chúng ta sẽ ăn ở đó trước khi xem phim phải không?
Đúng, nhưng chúng ta cần có mặt ở rạp chiếu phim lúc 6 giờ để mua vé.
Sau đó chúng ta có thể đi đến quán cà phê.
Ồ, được rồi.
2. Xem ngày tổ chức tiệc sinh nhật của Emma.
Bạn có dự tiệc sinh nhật lần thứ 20 của Emma vào tháng 6 không?
Đúng, nhưng thực ra là vào tháng Bảy.
Ồ, vâng, tất nhiên. Ngày 21 phải không?
Đúng vậy. Sinh nhật của cô ấy là ngày sau của tôi.
Đó là cách tôi nhớ nó.
Bây giờ hãy nghe lại.
Bạn có dự tiệc sinh nhật lần thứ 20 của Emma vào tháng 6 không?
Đúng, nhưng thực ra là vào tháng Bảy.
Ồ, vâng, tất nhiên. Ngày 21 phải không?
Đúng vậy. Sinh nhật của cô ấy là ngày sau của tôi.
Đó là cách tôi nhớ nó.
3. Đồng hồ của Nora ở đâu?
Mẹ có thấy đồng hồ của con không, mẹ? Tôi để nó trên giá sách.
Tôi nghĩ nó ở trong bếp, Nora, trên bàn.
Đó là đồng hồ của mẹ, mẹ ạ.
Ồ, vậy thì tôi đang mặc của bạn.
Xin lỗi, tôi tưởng nó là của tôi.
4. Giá vé tối nay bao nhiêu?
Đó là vé cho tối nay.
Vé cho đêm nay là vé cho đêm nay.
Tôi, ồ, cảm ơn bạn.
Tôi xin lỗi. Cô ấy đang thực hiện lại.
Cô ấy và Vanessa, người đã rủ tôi đi ngủ trưa trong bữa tiệc.
4. Giá vé xem trận tối nay là bao nhiêu?
Bạn có đi xem trận bóng rổ tối nay không?
Giá vé là bao nhiêu?
Hầu hết các tuần đều có giá £6, nhưng đó là mức giá đặc biệt tối nay.
£3,50, vậy thì hãy đến.
Phải. Tôi có £10 ở đây nên không sao cả.
Ka, 5.
Đâu là anh trai của con trai?
Nhìn kìa, anh trai tôi đằng kia đang nói chuyện với bạn bè anh ấy.
Ồ, anh ấy là người có mái tóc đen à?
Anh trai tôi có mái tóc vàng.
Ồ vâng, và anh ấy cũng đeo kính giống bạn.
Anh ấy trông rất đẹp.
Bây giờ hãy nghe lại.
Nhìn kìa, anh trai tôi đằng kia đang nói chuyện với bạn bè anh ấy.
Ồ, anh ấy là người có mái tóc đen à?
Anh trai tôi có mái tóc vàng.
Ồ vâng, và anh ấy cũng đeo kính giống bạn.
Anh ấy trông rất đẹp.
Đây là phần cuối của phần một.""",
    },
    {
        "id": 19,
        "title": "Her | She | Did",
        "icon": "🛍️",
        "file": "Bo tro 1 PART 2.mp3",
        "en": """Now look at part 2.
Listen to Amy telling her father about her shopping trip.
What did she and her friends buy?
For question 6 to 10, write a letter A to H next to each person.
You will hear the conversation twice.
Did you spend all your money Amy?
No dad, but we all bought something.
Look I found the video I wanted.
Great!
We spent hours in the department store.
Alison wants to take all her shoes on holiday and her suitcase is too small.
She bought a new one but it took her ages.
Then what did you do?
We went with Helen to look at mobile phones.
Her parents are getting her one for her birthday.
So she bought a magazine that had information about all the different kinds to show them.
That's a good idea.
Did Lucy find a present for her mum's birthday?
Yes, she looked at some beautiful shoes, but they were too expensive.
I think her mum will like the sweater she bought.
Oh good. What did Carrie buy?
A picture of our favourite band playing at a concert.
Is that the band you saw with Joe?
Yes, she got their new CD today.
The music magazines say it's excellent.
You must all be tired.
Now listen again.
Did you spend all your money, Amy?
No, Dad. But we all bought something.
Look, I found the video I wanted.
Great!
We spent hours in the department store.
Alison wants to take all her shoes on holiday and her suitcase is too small.
She bought a new one but it took her ages.
Then what did you do?
We went with Helen to look at mobile phones.
Her parents are getting her one for her birthday.
So she bought a magazine that had information about all the different kinds to show them.
That's a good idea.
Did Lucy find a present for her mum's birthday?
Yes, she looked at some beautiful shoes, but they were too expensive.
But I think her mum will like the sweater she bought.
Oh, good. What did Carrie buy?
A picture of our favourite band playing at a concert.
Is that the band you saw with Joe?
Yes, she got their new CD today.
The music magazines say it's excellent.
You must all be tired.
This is the end of part two.""",
        "vi": """Bây giờ hãy xem phần 2.
Hãy nghe Amy kể cho bố cô ấy nghe về chuyến đi mua sắm của cô ấy.
Cô ấy và bạn bè của cô ấy đã mua gì?
Đối với câu hỏi từ 6 đến 10, hãy viết chữ cái từ A đến H bên cạnh mỗi người.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Bạn đã tiêu hết tiền của mình chưa Amy?
Không có bố, nhưng tất cả chúng tôi đều mua thứ gì đó.
Nhìn này, tôi đã tìm thấy video tôi muốn.
Tuyệt vời!
Chúng tôi đã dành hàng giờ trong cửa hàng bách hóa.
Alison muốn mang hết giày đi nghỉ và vali của cô ấy quá nhỏ.
Cô ấy đã mua một cái mới nhưng phải mất nhiều thời gian.
Sau đó bạn đã làm gì?
Chúng tôi cùng Helen đi xem điện thoại di động.
Cha mẹ cô ấy đang tặng cô ấy một chiếc vào ngày sinh nhật của cô ấy.
Vì vậy cô ấy đã mua một tạp chí có thông tin về tất cả các loại khác nhau để cho họ xem.
Đó là một ý tưởng tốt.
Lucy đã tìm được quà cho ngày sinh nhật của mẹ cô ấy chưa?
Vâng, cô ấy đã xem một số đôi giày đẹp, nhưng chúng quá đắt.
Tôi nghĩ mẹ cô ấy sẽ thích chiếc áo len cô ấy mua.
Ồ tốt. Carrie đã mua gì?
Hình ảnh ban nhạc yêu thích của chúng tôi biểu diễn tại một buổi hòa nhạc.
Đó có phải là ban nhạc bạn đã xem cùng với Joe không?
Vâng, hôm nay cô ấy đã nhận được CD mới của họ.
Các tạp chí âm nhạc đều nói nó rất xuất sắc.
Chắc hẳn các bạn đều mệt mỏi rồi.
Bây giờ hãy nghe lại.
Bạn đã tiêu hết tiền của mình chưa, Amy?
Không, bố. Nhưng tất cả chúng tôi đã mua một cái gì đó.
Hãy nhìn xem, tôi đã tìm thấy video tôi muốn.
Tuyệt vời!
Chúng tôi đã dành hàng giờ trong cửa hàng bách hóa.
Alison muốn mang hết giày đi nghỉ và vali của cô ấy quá nhỏ.
Cô ấy đã mua một cái mới nhưng phải mất nhiều thời gian.
Sau đó bạn đã làm gì?
Chúng tôi cùng Helen đi xem điện thoại di động.
Cha mẹ cô ấy đang tặng cô ấy một chiếc vào ngày sinh nhật của cô ấy.
Vì vậy cô ấy đã mua một tạp chí có thông tin về tất cả các loại khác nhau để cho họ xem.
Đó là một ý tưởng tốt.
Lucy đã tìm được quà cho ngày sinh nhật của mẹ cô ấy chưa?
Vâng, cô ấy đã xem một số đôi giày đẹp, nhưng chúng quá đắt.
Nhưng tôi nghĩ mẹ cô ấy sẽ thích chiếc áo len cô ấy mua.
Ồ, tốt. Carrie đã mua gì?
Hình ảnh ban nhạc yêu thích của chúng tôi biểu diễn tại một buổi hòa nhạc.
Đó có phải là ban nhạc bạn đã xem cùng với Joe không?
Vâng, hôm nay cô ấy đã nhận được CD mới của họ.
Các tạp chí âm nhạc đều nói nó rất xuất sắc.
Chắc hẳn các bạn đều mệt mỏi rồi.
Đây là phần cuối của phần hai.""",
    },
    {
        "id": 20,
        "title": "Them | Like | Take",
        "icon": "🛌",
        "file": "Bo tro 1 PART 3.mp3",
        "en": """Now, look at part 3.
Listen to Jim talking to Sarah about things to take on holiday.
For questions 11 to 15, tick A, B or C.
You will hear the conversation twice.
Look at questions 11 to 15 now.
You have 20 seconds.
Now, listen to the conversation.
Hi Jim, I like your walking shoes.
I haven't seen any like them in England before.
They're Italian, Sarah.
I got them from my parents.
They're not like me.
They're not like me.
Now listen to the conversation.
Hi Jim, I like your walking shoes.
I haven't seen any like them in England before.
They're Italian, Sarah.
I got them from my holiday in Austria last month.
I need some like them.
Because I'm going to go there too.
Not many shops sell them.
I got mine at the market.
But they may have some at the new supermarket.
How much were they?
I think they usually cost 68 pounds.
But mine were only 48.
So I paid 20 pounds less.
That was really pleased.
I'll get some this afternoon.
Is there anything else special I should take?
Well, pack a hat.
Because the sun can be strong in the mountains.
I took a sweater and a jacket, but I never needed them.
Anything else?
Take lots of t-shirts.
One for each day you're going to go walking.
That's five days of my week's holiday.
And what about taking a phone?
Well, there'll be one in your hotel if you want to call home.
But take yours, because then you can call someone
if you get lost in the mountains.
Thanks, Jim.
No, listen again.
Hi, Jim. I like your walking shoes.
I haven't seen any like them in England before.
They're Italian, Sarah.
I got them from my holiday in Austria last month.
I need some like them.
Because I'm going to go there too.
Not many shops sell them.
I got mine at the market.
But they may have some at the new supermarket.
How much were they?
I think they usually cost 68 pounds.
But mine were only 48.
So I paid 20 pounds less.
That was really pleased.
I'll get some this afternoon.
Is there anything else special I should take?
Well, pack a hat, because the sun can be strong in the mountains.
I took a sweater and a jacket, but I never needed them.
Anything else?
Take lots of t-shirts.
One for each day you're going to go walking.
That's five days of my week's holiday.
And what about taking a phone?
Well, there'll be one in your hotel if you want to call home.
But take yours.
Because then you can call someone if you get lost in the mountains.
Thanks, Jim.
This is the end of part three.""",
        "vi": """Bây giờ hãy xem phần 3.
Hãy nghe Jim nói chuyện với Sarah về những việc cần làm trong kỳ nghỉ.
Đối với các câu hỏi từ 11 đến 15, đánh dấu A, B hoặc C.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Bây giờ hãy xem câu hỏi từ 11 đến 15.
Bạn có 20 giây.
Bây giờ, hãy lắng nghe cuộc trò chuyện.
Xin chào Jim, tôi thích đôi giày đi bộ của bạn.
Tôi chưa từng thấy cái nào giống như vậy ở Anh trước đây.
Họ là người Ý, Sarah.
Tôi đã nhận được chúng từ cha mẹ tôi.
Họ không giống tôi.
Họ không giống tôi.
Bây giờ hãy nghe cuộc trò chuyện.
Xin chào Jim, tôi thích đôi giày đi bộ của bạn.
Tôi chưa từng thấy cái nào giống như vậy ở Anh trước đây.
Họ là người Ý, Sarah.
Tôi đã nhận được chúng từ kỳ nghỉ ở Áo vào tháng trước.
Tôi cần một số như họ.
Vì tôi cũng sắp đi đến đó.
Không có nhiều cửa hàng bán chúng.
Tôi có cái của tôi ở chợ.
Nhưng họ có thể có một ít ở siêu thị mới.
Họ là bao nhiêu?
Tôi nghĩ chúng thường có giá 68 bảng.
Nhưng của tôi chỉ mới 48.
Vì thế tôi đã trả ít hơn 20 bảng.
Điều đó thực sự hài lòng.
Chiều nay tôi sẽ lấy một ít.
Có điều gì đặc biệt khác mà tôi nên dùng không?
Vâng, hãy đội một chiếc mũ.
Bởi vì mặt trời có thể mạnh ở vùng núi.
Tôi lấy một chiếc áo len và một chiếc áo khoác, nhưng tôi không bao giờ cần đến chúng.
Còn gì nữa không?
Lấy rất nhiều áo phông.
Một cho mỗi ngày bạn sẽ đi bộ.
Đó là năm ngày nghỉ trong tuần của tôi.
Còn việc lấy điện thoại thì sao?
Chà, sẽ có một cái trong khách sạn của bạn nếu bạn muốn gọi về nhà.
Nhưng hãy lấy của bạn, vì sau đó bạn có thể gọi cho ai đó
nếu bạn bị lạc trên núi.
Cảm ơn, Jim.
Không, nghe lại đi.
Chào Jim. Tôi thích đôi giày đi bộ của bạn.
Tôi chưa từng thấy cái nào giống như vậy ở Anh trước đây.
Họ là người Ý, Sarah.
Tôi đã nhận được chúng từ kỳ nghỉ ở Áo vào tháng trước.
Tôi cần một số như họ.
Vì tôi cũng sắp đi đến đó.
Không có nhiều cửa hàng bán chúng.
Tôi có cái của tôi ở chợ.
Nhưng họ có thể có một ít ở siêu thị mới.
Họ là bao nhiêu?
Tôi nghĩ chúng thường có giá 68 bảng.
Nhưng của tôi chỉ mới 48.
Vì thế tôi đã trả ít hơn 20 bảng.
Điều đó thực sự hài lòng.
Chiều nay tôi sẽ lấy một ít.
Có điều gì đặc biệt khác mà tôi nên dùng không?
Chà, hãy chuẩn bị sẵn mũ vì mặt trời có thể gay gắt trên núi.
Tôi lấy một chiếc áo len và một chiếc áo khoác, nhưng tôi không bao giờ cần đến chúng.
Còn gì nữa không?
Lấy rất nhiều áo phông.
Một cho mỗi ngày bạn sẽ đi bộ.
Đó là năm ngày nghỉ trong tuần của tôi.
Còn việc lấy điện thoại thì sao?
Chà, sẽ có một cái trong khách sạn của bạn nếu bạn muốn gọi về nhà.
Nhưng hãy lấy của bạn.
Bởi vì sau đó bạn có thể gọi cho ai đó nếu bạn bị lạc trên núi.
Cảm ơn, Jim.
Đây là phần cuối của phần ba.""",
    },
    {
        "id": 21,
        "title": "Part | Book | Homework",
        "icon": "💼",
        "file": "Bo tro 1 PART 4.mp3",
        "en": """Now look at part four.
You will hear Sally asking a friend about some homework.
Listen and complete question 16 to 20.
You will hear the conversation twice.
Hello Richard.
I wasn't at school today because I was ill.
Can you tell me what our biology homework is?
Yes Sally.
In class we talked about animals that live in water.
For homework we have to read a book about them.
The book's called Rivers.
It's in the school library.
Okay. Who is it by?
Let me see.
It's by Martin Cooper.
Is that C-O-O-P-E-R?
That's right.
You'll find the books on the third shelf on the biology book shelf.
We have to look at part seven.
Page is 123 to 127.
Okay. That's not very much.
What is it about?
That part's all about fish.
It's quite interesting.
Mrs. Knight says we're going to study lakes next week.
Oh right.
Do we have to read these pages for the lesson on Monday?
We have until Friday to do it.
Oh good. I'll go to the library on Thursday.
Thanks Richard. See you tomorrow.
Now listen again.
Hello Richard.
I wasn't at school today because I was ill.
Can you tell me what our biology homework is?
Yes Sally.
In class we talked about animals that live in water.
For homework we have to read a book about them.
The book's called Rivers.
It's in the school library.
Okay. Who is it by?
Let me see.
It's by Martin Cooper.
Is that C-O-O-P-E-R?
That's right.
You'll find the books on the third shelf on the biology book shelf.
We have to look at Part 7.
Pages 123 to 127.
Okay. That's not very much.
What is it about?
That part's all about fish.
It's quite interesting.
Mrs. Knight says we're going to study lakes next week.
Oh right.
We have to read these pages for the lesson on Monday.
We have until Friday to do it.
Oh good.
I'll go to the library on Thursday.
Thanks Richard. See you tomorrow.
This is the end of Part 4.""",
        "vi": """Bây giờ hãy xem phần bốn.
Bạn sẽ nghe thấy Sally hỏi một người bạn về bài tập về nhà.
Nghe và hoàn thành câu hỏi từ 16 đến 20.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Xin chào Richard.
Hôm nay tôi không đến trường vì tôi bị ốm.
Bạn có thể cho tôi biết bài tập sinh học của chúng tôi là gì không?
Vâng Sally.
Trong lớp chúng tôi đã nói về những động vật sống dưới nước.
Đối với bài tập về nhà chúng ta phải đọc một cuốn sách về họ.
Cuốn sách có tên là Những dòng sông.
Nó ở trong thư viện trường.
Được rồi. Nó là của ai?
Để tôi xem.
Đó là của Martin Cooper.
Đó có phải là C-O-O-P-E-R không?
Đúng vậy.
Bạn sẽ tìm thấy sách ở ngăn thứ ba trên kệ sách sinh học.
Chúng ta phải xem phần bảy.
Trang là 123 đến 127.
Được rồi. Đó không phải là nhiều lắm.
Nó nói về cái gì vậy?
Phần đó hoàn toàn là về cá.
Nó khá thú vị.
Bà Knight nói tuần tới chúng ta sẽ nghiên cứu về hồ.
Ồ đúng rồi.
Chúng ta có phải đọc những trang này cho bài học vào thứ Hai không?
Chúng ta có đến thứ Sáu để làm điều đó.
Ồ tốt. Tôi sẽ đến thư viện vào thứ năm.
Cảm ơn Richard. Hẹn gặp lại vào ngày mai.
Bây giờ hãy nghe lại.
Xin chào Richard.
Hôm nay tôi không đến trường vì tôi bị ốm.
Bạn có thể cho tôi biết bài tập sinh học của chúng tôi là gì không?
Vâng Sally.
Trong lớp chúng tôi đã nói về những động vật sống dưới nước.
Đối với bài tập về nhà chúng ta phải đọc một cuốn sách về họ.
Cuốn sách có tên là Những dòng sông.
Nó ở trong thư viện trường.
Được rồi. Nó là của ai?
Để tôi xem.
Đó là của Martin Cooper.
Đó có phải là C-O-O-P-E-R không?
Đúng vậy.
Bạn sẽ tìm thấy sách ở ngăn thứ ba trên kệ sách sinh học.
Chúng ta phải xem Phần 7.
Trang 123 đến 127.
Được rồi. Đó không phải là nhiều lắm.
Nó nói về cái gì vậy?
Phần đó hoàn toàn là về cá.
Nó khá thú vị.
Bà Knight nói tuần tới chúng ta sẽ nghiên cứu về hồ.
Ồ đúng rồi.
Chúng ta phải đọc những trang này cho bài học vào thứ Hai.
Chúng ta có đến thứ Sáu để làm điều đó.
Ồ tốt.
Tôi sẽ đến thư viện vào thứ năm.
Cảm ơn Richard. Hẹn gặp lại vào ngày mai.
Đây là phần cuối của Phần 4.""",
    },
    {
        "id": 22,
        "title": "Her | Now | Again",
        "icon": "🛸",
        "file": "Bo tro 2 PART 1.mp3",
        "en": """Now look at the instructions for part 1.
You will hear five short conversations.
You will hear each conversation twice.
There is one question for each conversation.
For questions 1 to 5, put a tick under the right answer.
There is an example.
How many people were at the meeting?
Were there many people at the meeting?
About 30.
That's not many.
No, but more than last time.
The answer is 30.
So there is a tick in box C.
Now we are ready to start.
What could question 1?
1.
What are they going to buy for Pam?
Last year we gave Pam a book for her birthday.
Should we buy her another one this year?
I think we should give her a plant or some chocolates.
But she doesn't like sweet things.
Let's get her something to put in her garden, but not a book again.
Now listen again.
Last year we gave Pam a book for her birthday.
Should we buy her another one this year?
I think we should give her a plant or some chocolates.
But she doesn't like sweet things.
Let's get her something to put in her garden, but not a book again.
2.
When is the man's appointment?
Good morning.
I'd like someone to cut my hair please.
Can I make an appointment?
Certainly.
Wednesday or Thursday morning or Friday afternoon?
On Friday I'm going to go to France.
What about Thursday afternoon?
I'm afraid I have a meeting all day Wednesday.
Well, it's a little difficult, but if that's the only afternoon you can come, we'll see
you then.
Now listen again.
Good morning.
I'd like someone to cut my hair please.
Can I make an appointment?
Certainly.
Um, Wednesday or Thursday morning or Friday afternoon?
On Friday I'm going to go to France.
What about Thursday afternoon?
I'm afraid I have a meeting all day Wednesday.
Well, it's a little difficult, but if that's the only afternoon you can come, we'll see
you then.
3.
Which is the aunt's postcard?
Looks, Andrew.
I've got this really nice postcard from my aunt.
Oh, what a pretty village and it's right by a river.
Is it in the mountains?
Yes, but you can't see them in the picture.
Hmm, perhaps they're behind those tall trees.
Now listen again.
Looks, Andrew.
I've got this really nice postcard from my aunt.
Oh, what a pretty village and it's right by a river.
Is it in the mountains?
Yes, but you can't see them in the picture.
Hmm, perhaps they're behind those tall trees.
4.
What time will the plane to Milan leave?
Excuse me.
What time is the next plane to Milan?
It should leave at quarter past seven, but it's an hour late today.
Oh, that's a problem.
If it doesn't leave until quarter past eight, I'll be one hour late for my meeting.
I'm sorry, sir.
There's nothing I can do.
Now listen again.
Excuse me.
What time is the next plane to Milan?
It should leave at quarter past seven, but it's an hour late today.
Oh, that's a problem.
If it doesn't leave until quarter past eight, I'll be one hour late for my meeting.
I'm sorry, sir.
There's nothing I can do.
5.
What does Joe's father do?
What's your father's job, Joe?
He was a pilot, but now he's a farmer.
What about your father?
He's a photographer.
Oh, I want to do that.
If I don't become a pilot, now listen again.
What's your father's job, Joe?
He was a pilot, but now he's a farmer.
What about your father?
He's a photographer.
Oh, I want to do that.
If I don't become a pilot.
This is the end of part one.""",
        "vi": """Bây giờ hãy xem hướng dẫn cho phần 1.
Bạn sẽ nghe thấy năm đoạn hội thoại ngắn.
Bạn sẽ nghe mỗi cuộc trò chuyện hai lần.
Có một câu hỏi cho mỗi cuộc trò chuyện.
Đối với các câu hỏi từ 1 đến 5, hãy đánh dấu vào câu trả lời đúng.
Có một ví dụ.
Có bao nhiêu người ở cuộc họp?
Có nhiều người ở cuộc họp không?
Khoảng 30.
Đó không phải là nhiều.
Không, nhưng nhiều hơn lần trước.
Câu trả lời là 30.
Vậy là có dấu tích ở ô C.
Bây giờ chúng ta đã sẵn sàng để bắt đầu.
Câu hỏi 1 có thể là gì?
1.
Họ định mua gì cho Pam?
Năm ngoái chúng tôi đã tặng Pam một cuốn sách nhân dịp sinh nhật cô ấy.
Chúng ta có nên mua cho cô ấy một chiếc khác trong năm nay không?
Tôi nghĩ chúng ta nên tặng cô ấy một cái cây hoặc một ít sôcôla.
Nhưng cô ấy không thích đồ ngọt.
Hãy kiếm cho cô ấy thứ gì đó để đặt trong vườn, nhưng không phải là một cuốn sách nữa.
Bây giờ hãy nghe lại.
Năm ngoái chúng tôi đã tặng Pam một cuốn sách nhân dịp sinh nhật cô ấy.
Chúng ta có nên mua cho cô ấy một chiếc khác trong năm nay không?
Tôi nghĩ chúng ta nên tặng cô ấy một cái cây hoặc một ít sôcôla.
Nhưng cô ấy không thích đồ ngọt.
Hãy kiếm cho cô ấy thứ gì đó để đặt trong vườn, nhưng không phải là một cuốn sách nữa.
2.
Cuộc hẹn của người đàn ông là khi nào?
Chào buổi sáng.
Tôi muốn ai đó cắt tóc cho tôi.
Tôi có thể đặt lịch hẹn được không?
Chắc chắn.
Sáng thứ Tư hay thứ Năm hay chiều thứ Sáu?
Thứ Sáu tôi sẽ đi Pháp.
Thế còn chiều thứ Năm thì sao?
Tôi e là tôi phải họp cả ngày thứ Tư.
Chà, hơi khó một chút, nhưng nếu đó là buổi chiều duy nhất bạn có thể đến, chúng ta sẽ xem
thì bạn.
Bây giờ hãy nghe lại.
Chào buổi sáng.
Tôi muốn ai đó cắt tóc cho tôi.
Tôi có thể đặt lịch hẹn được không?
Chắc chắn.
Ừm, sáng thứ Tư hay thứ Năm hay chiều thứ Sáu?
Thứ Sáu tôi sẽ đi Pháp.
Thế còn chiều thứ Năm thì sao?
Tôi e là tôi phải họp cả ngày thứ Tư.
Chà, hơi khó một chút, nhưng nếu đó là buổi chiều duy nhất bạn có thể đến, chúng ta sẽ xem
thì bạn.
3.
Bưu thiếp của dì là gì?
Trông kìa, Andrew.
Tôi nhận được tấm bưu thiếp rất đẹp này từ dì tôi.
Ồ, thật là một ngôi làng xinh đẹp và nó nằm ngay cạnh một con sông.
Có phải ở trên núi không?
Có, nhưng bạn không thể nhìn thấy chúng trong ảnh.
Hmm, có lẽ họ ở đằng sau những cái cây cao đó.
Bây giờ hãy nghe lại.
Trông kìa, Andrew.
Tôi nhận được tấm bưu thiếp rất đẹp này từ dì tôi.
Ồ, thật là một ngôi làng xinh đẹp và nó nằm ngay cạnh một con sông.
Có phải ở trên núi không?
Có, nhưng bạn không thể nhìn thấy chúng trong ảnh.
Hmm, có lẽ họ ở đằng sau những cái cây cao đó.
4.
Máy bay tới Milan sẽ khởi hành lúc mấy giờ?
Xin lỗi.
Chuyến bay tiếp theo tới Milan khởi hành lúc mấy giờ?
Lẽ ra nó sẽ khởi hành lúc bảy giờ mười lăm, nhưng hôm nay đã muộn một tiếng.
Ồ, đó là một vấn đề.
Nếu nó không khởi hành trước 8 giờ 15, tôi sẽ trễ cuộc họp một tiếng.
Tôi xin lỗi, thưa ngài.
Tôi không thể làm gì được.
Bây giờ hãy nghe lại.
Xin lỗi.
Chuyến bay tiếp theo tới Milan khởi hành lúc mấy giờ?
Lẽ ra nó sẽ khởi hành lúc bảy giờ mười lăm, nhưng hôm nay đã muộn một tiếng.
Ồ, đó là một vấn đề.
Nếu nó không khởi hành trước 8 giờ 15, tôi sẽ trễ cuộc họp một tiếng.
Tôi xin lỗi, thưa ngài.
Tôi không thể làm gì được.
5.
Bố của Joe làm nghề gì?
Công việc của bố bạn là gì, Joe?
Anh ấy từng là phi công nhưng giờ anh ấy là nông dân.
Còn bố của bạn thì sao?
Anh ấy là một nhiếp ảnh gia.
Ồ, tôi muốn làm điều đó.
Nếu tôi không trở thành phi công, bây giờ hãy nghe lại.
Công việc của bố bạn là gì, Joe?
Anh ấy từng là phi công nhưng giờ anh ấy là nông dân.
Còn bố của bạn thì sao?
Anh ấy là một nhiếp ảnh gia.
Ồ, tôi muốn làm điều đó.
Nếu tôi không trở thành phi công.
Đây là phần cuối của phần một.""",
    },
    {
        "id": 23,
        "title": "She | Lot | Did",
        "icon": "📚",
        "file": "Bo tro 2 PART 2.mp3",
        "en": """Now look at part 2.
Listen to Sarah and Matthew talking about the people they met at a party.
What do they say about each person?
For question 6 to 10, write a letter A to H next to each person.
You will hear the conversation twice.
Did you like the party Sarah?
Yes Matthew, I met a lot of people.
Did you see Jenny, the girl with a short blonde hair?
I think so.
Was she talking to John at the beginning of the evening?
Yes, I tried to speak to him later, but he didn't say much.
He's okay, he just prefers not to talk a lot.
Who was the girl who arrived late?
She was very friendly, she knew everyone.
That was Mary, she's certainly not quiet.
I know her brother Bob, he was there too.
He's still at school isn't he?
Everyone was a lot older than him, but he didn't mind.
Another person I liked was David.
Is he rather short?
Not at all, he was taller than everybody there.
Who else did you meet?
Sally, she's travelled all over the world and knows a lot of famous people.
Everything she said was interesting.
It was a good party.
Now listen again.
Did you like the party Sarah?
Yes Matthew, I met a lot of people.
Did you see Jenny, the girl with a short blonde hair?
I think so.
Was she talking to John at the beginning of the evening?
Yes, I tried to speak to him later, but he didn't say much.
He's okay, he just prefers not to talk a lot.
Who was the girl who arrived late?
She was very friendly, she knew everyone.
That was Mary, she's certainly not quiet.
I know her brother Bob, he was there too.
He's still at school isn't he?
Yes, everyone was a lot older than him, but he didn't mind.
Another person I liked was David.
Is he rather short?
Not at all, he was taller than everybody there.
Who else did you meet?
Sally, she's travelled all over the world and knows a lot of famous people.
Everything she said was interesting.
It was a good party.
This is the end of part two.
The end of part two.""",
        "vi": """Bây giờ hãy xem phần 2.
Hãy nghe Sarah và Matthew kể về những người họ gặp ở một bữa tiệc.
Họ nói gì về mỗi người?
Đối với câu hỏi từ 6 đến 10, hãy viết chữ cái từ A đến H bên cạnh mỗi người.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Bạn có thích bữa tiệc không Sarah?
Vâng Matthew, tôi đã gặp rất nhiều người.
Bạn có thấy Jenny, cô gái có mái tóc ngắn màu vàng không?
Tôi nghĩ vậy.
Cô ấy có nói chuyện với John vào đầu buổi tối không?
Vâng, sau này tôi đã cố gắng nói chuyện với anh ấy, nhưng anh ấy không nói nhiều.
Anh ấy ổn, anh ấy chỉ thích không nói nhiều.
Cô gái đến muộn là ai?
Cô ấy rất thân thiện, cô ấy biết tất cả mọi người.
Đó là Mary, cô ấy chắc chắn không im lặng.
Tôi biết anh trai Bob của cô ấy, anh ấy cũng ở đó.
Anh ấy vẫn còn ở trường phải không?
Mọi người đều lớn tuổi hơn anh rất nhiều, nhưng anh không bận tâm.
Một người khác mà tôi thích là David.
Anh ấy khá lùn phải không?
Không hề, anh ấy cao hơn mọi người ở đó.
Bạn còn gặp ai nữa?
Sally, cô ấy đã đi du lịch khắp thế giới và biết rất nhiều người nổi tiếng.
Mọi điều cô ấy nói đều thú vị.
Đó là một bữa tiệc tốt.
Bây giờ hãy nghe lại.
Bạn có thích bữa tiệc không Sarah?
Vâng Matthew, tôi đã gặp rất nhiều người.
Bạn có thấy Jenny, cô gái có mái tóc ngắn màu vàng không?
Tôi nghĩ vậy.
Cô ấy có nói chuyện với John vào đầu buổi tối không?
Vâng, sau này tôi đã cố gắng nói chuyện với anh ấy, nhưng anh ấy không nói nhiều.
Anh ấy ổn, anh ấy chỉ thích không nói nhiều.
Cô gái đến muộn là ai?
Cô ấy rất thân thiện, cô ấy biết tất cả mọi người.
Đó là Mary, cô ấy chắc chắn không im lặng.
Tôi biết anh trai Bob của cô ấy, anh ấy cũng ở đó.
Anh ấy vẫn còn ở trường phải không?
Đúng, mọi người đều lớn tuổi hơn anh rất nhiều, nhưng anh không bận tâm.
Một người khác mà tôi thích là David.
Anh ấy khá lùn phải không?
Không hề, anh ấy cao hơn mọi người ở đó.
Bạn còn gặp ai nữa?
Sally, cô ấy đã đi du lịch khắp thế giới và biết rất nhiều người nổi tiếng.
Mọi điều cô ấy nói đều thú vị.
Đó là một bữa tiệc tốt.
Đây là phần cuối của phần hai.
Sự kết thúc của phần hai.""",
    },
    {
        "id": 24,
        "title": "Course | College | Now",
        "icon": "💳",
        "file": "Bo tro 2 PART 3.mp3",
        "en": """Now look at part 3.
Listen to Philip talking to a friend about his photography course.
For questions 11 to 15, tick A, B or C.
You will hear the conversation twice.
Look at questions 11 to 15 now.
You have 20 seconds.
Now listen to the conversation.
Hello Philip.
Are you doing a photography course?
Yes.
There wasn't one at my college, park college, so I go to city college in south road.
Are you classes in the evening?
Yes.
I finish at park college at quarter past five and get home about six.
The lessons start at quarter to seven.
I have just enough time to eat.
How much are they?
My ten week course is usually 95 pounds, but it costs me 75 pounds because I'm a student.
There's also a five week course for 55 pounds.
Is it a good course?
Yes, great.
The cameras are rather old, but my photos are much better now, so I'm really pleased.
I'll never be a famous photographer though.
I think taking photographs is difficult.
Well, we did animals first, and they're certainly not easy.
But then we took pictures of trees, and that wasn't difficult.
We'll photograph children next.
And after the course?
There aren't many jobs for photographers.
It'll be my hobby.
I can use my father's camera, but I'll have to buy a lot of film.
Now listen again.
Hello Philip.
Are you doing a photography course?
Yes.
There wasn't one at my college, park college, so I go to city college in south road.
Are you classes in the evening?
Yes, I finish at park college at quarter past five, and get home about six.
The lessons start at quarter to seven.
I have just enough time to eat.
How much are they?
My ten week course is usually 95 pounds, but it costs me 75 pounds because I'm a student.
There's also a five week course for 55 pounds.
Is it a good course?
Yes, great.
The cameras are rather old, but my photos are much better now, so I'm really pleased.
I'll never be a famous photographer, though.
I think taking photographs is difficult.
Well, we did animals first, and they're certainly not easy.
But then we took pictures of trees, and that wasn't difficult.
We'll photograph children next.
And after the course?
There aren't many jobs for photographers. It'll be my hobby.
I can use my father's camera, but I'll have to buy a lot of film.
This is the end of part three.""",
        "vi": """Bây giờ hãy xem phần 3.
Hãy nghe Philip nói chuyện với một người bạn về khóa học nhiếp ảnh của anh ấy.
Đối với các câu hỏi từ 11 đến 15, đánh dấu A, B hoặc C.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Bây giờ hãy xem câu hỏi từ 11 đến 15.
Bạn có 20 giây.
Bây giờ hãy nghe cuộc trò chuyện.
Xin chào Philip.
Bạn đang tham gia một khóa học nhiếp ảnh?
Đúng.
Không có trường nào ở trường đại học của tôi, trường đại học park, nên tôi vào trường cao đẳng thành phố ở đường phía nam.
Bạn có lớp học vào buổi tối không?
Đúng.
Tôi học xong ở trường đại học Park lúc năm giờ mười lăm và về nhà vào khoảng sáu giờ.
Các bài học bắt đầu lúc bảy giờ kém mười lăm.
Tôi chỉ có đủ thời gian để ăn.
Chúng giá bao nhiêu?
Khóa học 10 tuần của tôi thường có giá 95 bảng, nhưng tôi phải trả 75 bảng vì tôi là sinh viên.
Ngoài ra còn có một khóa học 5 tuần với giá 55 pound.
Đây có phải là một khóa học tốt?
Vâng, tuyệt vời.
Máy ảnh khá cũ nhưng ảnh của tôi bây giờ đẹp hơn nhiều nên tôi rất hài lòng.
Tuy nhiên, tôi sẽ không bao giờ trở thành một nhiếp ảnh gia nổi tiếng.
Tôi nghĩ việc chụp ảnh là khó khăn.
Chà, chúng tôi đã làm động vật trước tiên và chúng chắc chắn không hề dễ dàng.
Nhưng sau đó chúng tôi chụp ảnh cây cối và việc đó không khó khăn gì.
Tiếp theo chúng ta sẽ chụp ảnh trẻ em.
Và sau khóa học?
Không có nhiều việc làm cho nhiếp ảnh gia.
Nó sẽ là sở thích của tôi.
Tôi có thể sử dụng máy ảnh của bố tôi nhưng tôi sẽ phải mua rất nhiều phim.
Bây giờ hãy nghe lại.
Xin chào Philip.
Bạn đang tham gia một khóa học nhiếp ảnh?
Đúng.
Không có trường nào ở trường đại học của tôi, trường đại học park, nên tôi vào trường cao đẳng thành phố ở đường phía nam.
Bạn có lớp học vào buổi tối không?
Vâng, tôi học xong ở trường đại học Park vào lúc 5 giờ 15 và về nhà vào khoảng 6 giờ.
Các bài học bắt đầu lúc bảy giờ kém mười lăm.
Tôi chỉ có đủ thời gian để ăn.
Chúng giá bao nhiêu?
Khóa học 10 tuần của tôi thường có giá 95 bảng, nhưng tôi phải trả 75 bảng vì tôi là sinh viên.
Ngoài ra còn có một khóa học 5 tuần với giá 55 pound.
Đây có phải là một khóa học tốt?
Vâng, tuyệt vời.
Máy ảnh khá cũ nhưng ảnh của tôi bây giờ đẹp hơn nhiều nên tôi rất hài lòng.
Tuy nhiên, tôi sẽ không bao giờ trở thành một nhiếp ảnh gia nổi tiếng.
Tôi nghĩ việc chụp ảnh là khó khăn.
Chà, chúng tôi đã làm động vật trước tiên và chúng chắc chắn không hề dễ dàng.
Nhưng sau đó chúng tôi chụp ảnh cây cối và việc đó không khó khăn gì.
Tiếp theo chúng ta sẽ chụp ảnh trẻ em.
Và sau khóa học?
Không có nhiều việc làm cho nhiếp ảnh gia. Nó sẽ là sở thích của tôi.
Tôi có thể sử dụng máy ảnh của bố tôi nhưng tôi sẽ phải mua rất nhiều phim.
Đây là phần cuối của phần ba.""",
    },
    {
        "id": 25,
        "title": "Class | Now | Friend",
        "icon": "👗",
        "file": "Bo tro 2 PART 4.mp3",
        "en": """Now look at part four.
You will hear a man asking for information about the Westwood English school.
Listen and complete questions 16 to 20.
You will hear the conversation twice.
Westwood English school?
Hello. I want to ask about evening classes please.
Yes, they're on Thursdays, but this term will finish at the end of August.
We'll start again on the 22nd of September, but you can book your place now.
It's for a Chinese friend. He wants an easy class.
Well, there's a two hour class for beginners.
My friend would like something shorter.
Well, we have a 50 minute speaking class. That would be good for him.
The teacher is Miss Jarvis. That's J-A-R-V-I-S.
The student's all like her.
How much does that class cost?
It's £7.50 per class.
Or if you pay for all 12 classes now, it's only £78.
It's cheaper that way.
Right.
Can your friend come to the school soon and book his place?
The address is 223 Fitzroy Square.
Is that in the centre of town?
Well, it's about 20 minutes walk from the station.
We're just by the bookshop.
Right. Thank you.
Goodbye.
Now listen again.
Westwood English school?
Hello. I want to ask about evening classes, please.
Yes. They're on Thursdays.
But this term will finish at the end of August.
We'll start again on the 22nd of September.
But you can book your place now.
It's for a Chinese friend. He wants an easy class.
Well, there's a two hour class for beginners.
My friend would like something shorter.
Well, we have a 50 minute speaking class.
That would be good for him.
The teacher is Miss Jarvis.
That's J-A-R-V-I-S.
The students all like her.
How much does that class cost?
It's £7.50 per class.
Or if you pay for all 12 classes now, it's only £78.
It's cheaper that way.
Right.
Can your friend come to the school soon and book his place?
The address is 223 Fitzroy Square.
Is that in the centre of town?
Well, it's about 20 minutes walk from the station.
We're just by the book shop.
Right. Thank you.
Goodbye.
This is the end of part four.
Thank you.""",
        "vi": """Bây giờ hãy xem phần bốn.
Bạn sẽ nghe thấy một người đàn ông hỏi thông tin về trường Anh ngữ Westwood.
Nghe và hoàn thành các câu hỏi từ 16 đến 20.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Trường Anh ngữ Westwood?
Xin chào. Mình muốn hỏi về lớp học buổi tối.
Vâng, họ tổ chức vào thứ Năm, nhưng học kỳ này sẽ kết thúc vào cuối tháng Tám.
Chúng tôi sẽ bắt đầu lại vào ngày 22 tháng 9, nhưng bạn có thể đặt chỗ ngay bây giờ.
Nó dành cho một người bạn Trung Quốc. Anh ấy muốn một lớp học dễ dàng.
Vâng, có một lớp học kéo dài hai giờ dành cho người mới bắt đầu.
Bạn tôi muốn cái gì đó ngắn hơn.
À, chúng ta có một lớp học nói 50 phút. Điều đó sẽ tốt cho anh ấy.
Giáo viên là cô Jarvis. Đó là J-A-R-V-I-S.
Học sinh nào cũng giống cô ấy.
Lớp học đó có giá bao nhiêu?
Đó là £ 7,50 mỗi lớp.
Hoặc nếu bây giờ bạn trả tiền cho tất cả 12 lớp thì chỉ còn £78.
Cách đó rẻ hơn.
Phải.
Bạn của bạn có thể đến trường sớm và đặt chỗ được không?
Địa chỉ là 223 Quảng trường Fitzroy.
Đó có phải là ở trung tâm thị trấn không?
À, cách ga khoảng 20 phút đi bộ.
Chúng tôi đang ở cạnh hiệu sách.
Phải. Cảm ơn.
Tạm biệt.
Bây giờ hãy nghe lại.
Trường Anh ngữ Westwood?
Xin chào. Mình muốn hỏi về lớp học buổi tối.
Đúng. Họ đang vào thứ Năm.
Nhưng học kỳ này sẽ kết thúc vào cuối tháng 8.
Chúng ta sẽ bắt đầu lại vào ngày 22 tháng 9.
Nhưng bạn có thể đặt chỗ ngay bây giờ.
Nó dành cho một người bạn Trung Quốc. Anh ấy muốn một lớp học dễ dàng.
Vâng, có một lớp học kéo dài hai giờ dành cho người mới bắt đầu.
Bạn tôi muốn cái gì đó ngắn hơn.
À, chúng ta có một lớp học nói 50 phút.
Điều đó sẽ tốt cho anh ấy.
Giáo viên là cô Jarvis.
Đó là J-A-R-V-I-S.
Các sinh viên đều thích cô ấy.
Lớp học đó có giá bao nhiêu?
Đó là £ 7,50 mỗi lớp.
Hoặc nếu bây giờ bạn trả tiền cho tất cả 12 lớp thì chỉ còn £78.
Cách đó rẻ hơn.
Phải.
Bạn của bạn có thể đến trường sớm và đặt chỗ được không?
Địa chỉ là 223 Quảng trường Fitzroy.
Đó có phải là ở trung tâm thị trấn không?
À, cách ga khoảng 20 phút đi bộ.
Chúng tôi đang ở gần hiệu sách.
Phải. Cảm ơn.
Tạm biệt.
Đây là phần cuối của phần bốn.
Cảm ơn.""",
    },
    {
        "id": 26,
        "title": "One | Take | Time",
        "icon": "💺",
        "file": "Bo tro 3 PART 1.mp3",
        "en": """Now look at the instructions for part 1.
You will hear five short conversations.
You will hear each conversation twice.
There is one question for each conversation.
For questions 1 to 5, put a tick under the right answer.
Here is an example.
How many people were at the meeting?
Were there many people at the meeting?
About 30.
That's not many.
No, but more than last time.
The answer is 30, so there is a tick in box C.
Now we are ready to start.
Look at question 1.
1.
How much is the car?
So which car are you buying?
The Monarch 2000.
It's lovely, but I have to get a thousand pounds more from the bank first, because I don't
have enough money.
It's a lot of money, three thousand pounds.
I could live on that for a year.
Well, cars are expensive.
Now listen again.
So which car are you buying?
The Monarch 2000.
It's lovely, but I have to get a thousand pounds more from the bank first, because I don't
have enough money.
It's a lot of money, three thousand pounds.
I could live on that for a year.
Well, cars are expensive.
2.
What's Eleanor going to take to the party?
Hi Eleanor, are you taking some cans of cola to the party?
Of course, and a pizza.
I'm going to take a big bottle of orange juice and some biscuits.
Chocolate ones, I hope.
3.
Where will Susan buy her eggs?
We need some more eggs, Susan.
I'll take the other one.
I'll take the other one.
I'll take the other one.
I'll take the other one.
I'll take the other one.
I'll drive out to the farm and get them tomorrow.
It'll be quicker to go to the market, or to the little shop across the road.
I know, but I prefer to know that they haven't been on the shelves for a long time.
Now listen again.
We need some more eggs, Susan.
I'll drive out to the farm and get them tomorrow.
It'll be quicker to go to the market, or to the little shop across the road.
I know, but I prefer to know that they haven't been on the shelves for a long time.
4.
What time does the film begin?
Would you like to see a film this afternoon?
OK, what time?
It starts at quarter to two, but we need tickets.
So let's meet at the cinema at quarter past one.
How long is the film?
One and a half hours.
Now listen again.
Would you like to see a film this afternoon?
OK, what time?
It starts at quarter to two, but we need tickets.
So let's meet at the cinema at quarter past one.
How long is the film?
One and a half hours.
5.
How will the man travel to London?
We drove to London last weekend.
Really? I'm going to go there for the day tomorrow.
Oh yes. Are you going by coach?
It's the best way.
There's a fast train, but it's too expensive for me.
This is the end of part one.
Thank you.""",
        "vi": """Bây giờ hãy xem hướng dẫn cho phần 1.
Bạn sẽ nghe thấy năm đoạn hội thoại ngắn.
Bạn sẽ nghe mỗi cuộc trò chuyện hai lần.
Có một câu hỏi cho mỗi cuộc trò chuyện.
Đối với các câu hỏi từ 1 đến 5, hãy đánh dấu vào câu trả lời đúng.
Đây là một ví dụ.
Có bao nhiêu người ở cuộc họp?
Có nhiều người ở cuộc họp không?
Khoảng 30.
Đó không phải là nhiều.
Không, nhưng nhiều hơn lần trước.
Đáp án là 30 nên đánh dấu vào ô C.
Bây giờ chúng ta đã sẵn sàng để bắt đầu.
Nhìn vào câu hỏi 1.
1.
Chiếc xe bao nhiêu tiền?
Vậy bạn mua xe nào?
Vua 2000.
Thật đáng yêu, nhưng trước tiên tôi phải kiếm thêm một nghìn bảng nữa từ ngân hàng, vì tôi không
có đủ tiền.
Đó là rất nhiều tiền, ba nghìn bảng.
Tôi có thể sống với điều đó trong một năm.
Vâng, xe hơi đắt tiền.
Bây giờ hãy nghe lại.
Vậy bạn mua xe nào?
Vua 2000.
Thật đáng yêu, nhưng trước tiên tôi phải kiếm thêm một nghìn bảng nữa từ ngân hàng, vì tôi không
có đủ tiền.
Đó là rất nhiều tiền, ba nghìn bảng.
Tôi có thể sống với điều đó trong một năm.
Vâng, xe hơi đắt tiền.
2.
Eleanor sẽ mang gì tới bữa tiệc?
Xin chào Eleanor, bạn có mang vài lon cola đến bữa tiệc không?
Tất nhiên, và một chiếc bánh pizza.
Tôi sẽ lấy một chai nước cam lớn và một ít bánh quy.
Tôi hy vọng là sô cô la.
3.
Susan sẽ mua trứng ở đâu?
Chúng ta cần thêm trứng, Susan.
Tôi sẽ lấy cái khác.
Tôi sẽ lấy cái khác.
Tôi sẽ lấy cái khác.
Tôi sẽ lấy cái khác.
Tôi sẽ lấy cái khác.
Ngày mai tôi sẽ lái xe tới trang trại và lấy chúng.
Sẽ nhanh hơn nếu đi chợ hoặc đến cửa hàng nhỏ bên kia đường.
Tôi biết, nhưng tôi muốn biết rằng chúng đã không còn trên kệ từ lâu rồi.
Bây giờ hãy nghe lại.
Chúng ta cần thêm trứng, Susan.
Ngày mai tôi sẽ lái xe tới trang trại và lấy chúng.
Sẽ nhanh hơn nếu đi chợ hoặc đến cửa hàng nhỏ bên kia đường.
Tôi biết, nhưng tôi muốn biết rằng chúng đã không còn trên kệ từ lâu rồi.
4.
Phim bắt đầu lúc mấy giờ?
Bạn có muốn xem phim chiều nay không?
Được rồi, mấy giờ?
Nó bắt đầu lúc hai giờ kém mười lăm, nhưng chúng ta cần vé.
Vậy hãy gặp nhau ở rạp chiếu phim lúc một giờ mười lăm nhé.
Phim dài bao nhiêu?
Một tiếng rưỡi.
Bây giờ hãy nghe lại.
Bạn có muốn xem phim chiều nay không?
Được rồi, mấy giờ?
Nó bắt đầu lúc hai giờ kém mười lăm, nhưng chúng ta cần vé.
Vậy hãy gặp nhau ở rạp chiếu phim lúc một giờ mười lăm nhé.
Phim dài bao nhiêu?
Một tiếng rưỡi.
5.
Người đàn ông sẽ tới London bằng cách nào?
Chúng tôi lái xe đến London vào cuối tuần trước.
Thật sự? Tôi sẽ đến đó vào ngày mai.
Ồ vâng. Bạn có đi bằng xe khách không?
Đó là cách tốt nhất.
Có một chuyến tàu nhanh nhưng nó quá đắt đối với tôi.
Đây là phần cuối của phần một.
Cảm ơn.""",
    },
    {
        "id": 27,
        "title": "Too | Sports | Centre",
        "icon": "🛎️",
        "file": "Bo tro 3 PART 2.mp3",
        "en": """Now look at part 2.
Listen to Sarah talking to a friend about a sports centre.
What is the problem with the different things at the sports centre?
For questions 6 to 10 write a letter A to H next to each thing.
You will hear the conversation twice.
I like your new t-shirt Sarah.
The colours are nice but the problem is it's too big.
I got it from the shop at the sports centre.
I went swimming there because it was a hot day but it was too noisy for me.
There were a lot of people in the pool.
So was it difficult to find a space in the car park there?
Yes. It's not big enough.
Did you go to the cafe?
Yes for a cold drink.
But I didn't stay. The tables and floor weren't clean.
But I hear they have a good football club there.
That's right. My brother wanted to go but it starts too late in the evening for him.
It's a pity because it's not an expensive club.
Can you learn tennis there?
I called about lessons but they cost too much.
I'll teach you tennis but not today. It's too hot.
Let's go for a cold swim in the river.
Now listen again.
I like your new t-shirt Sarah.
The colors are nice but the problem is it's too big.
I got it from the shop at the sports centre.
I went swimming there because it was a hot day but it was too noisy for me.
There were a lot of people in the pool.
So was it difficult to find a space in the car park there?
Yes. It's not big enough.
Did you go to the cafe?
Yes for a cold drink.
But I didn't stay. The tables and floor weren't clean.
Ugh. But I hear they have a good football club there.
That's right. My brother wanted to go but it starts too late in the evening for him.
It's a pity because it's not an expensive club.
Can you learn tennis there?
I called about lessons but they cost too much.
I'll teach you tennis but not today. It's too hot.
Let's go for a cold swim in the river.
This is the end of part two.""",
        "vi": """Bây giờ hãy xem phần 2.
Nghe Sarah nói chuyện với một người bạn về một trung tâm thể thao.
Vấn đề với những điều khác nhau ở trung tâm thể thao là gì?
Đối với các câu hỏi từ 6 đến 10, hãy viết chữ cái từ A đến H bên cạnh mỗi điều.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Tôi thích chiếc áo phông mới của bạn Sarah.
Màu sắc đẹp nhưng vấn đề là nó quá lớn.
Tôi mua nó từ cửa hàng ở trung tâm thể thao.
Tôi đã đi bơi ở đó vì trời nắng nóng nhưng lại quá ồn ào đối với tôi.
Có rất nhiều người trong hồ bơi.
Vậy tìm chỗ đậu xe ở đó có khó không?
Đúng. Nó không đủ lớn.
Bạn đã đến quán cà phê chưa?
Có cho một thức uống lạnh.
Nhưng tôi đã không ở lại. Bàn và sàn không sạch sẽ.
Nhưng tôi nghe nói ở đó có một câu lạc bộ bóng đá rất tốt.
Đúng vậy. Anh trai tôi muốn đi nhưng trời đã quá muộn đối với anh ấy.
Thật đáng tiếc vì đây không phải là một câu lạc bộ đắt tiền.
Bạn có thể học quần vợt ở đó không?
Tôi đã gọi điện về các bài học nhưng chúng đắt quá.
Tôi sẽ dạy bạn quần vợt nhưng không phải hôm nay. Trời nóng quá.
Chúng ta hãy đi bơi lạnh trên sông.
Bây giờ hãy nghe lại.
Tôi thích chiếc áo phông mới của bạn Sarah.
Màu sắc đẹp nhưng vấn đề là nó quá lớn.
Tôi mua nó từ cửa hàng ở trung tâm thể thao.
Tôi đã đi bơi ở đó vì trời nắng nóng nhưng lại quá ồn ào đối với tôi.
Có rất nhiều người trong hồ bơi.
Vậy tìm chỗ đậu xe ở đó có khó không?
Đúng. Nó không đủ lớn.
Bạn đã đến quán cà phê chưa?
Có cho một thức uống lạnh.
Nhưng tôi đã không ở lại. Bàn và sàn không sạch sẽ.
Ờ. Nhưng tôi nghe nói ở đó có một câu lạc bộ bóng đá rất tốt.
Đúng vậy. Anh trai tôi muốn đi nhưng trời đã quá muộn đối với anh ấy.
Thật đáng tiếc vì đây không phải là một câu lạc bộ đắt tiền.
Bạn có thể học quần vợt ở đó không?
Tôi đã gọi điện về các bài học nhưng chúng đắt quá.
Tôi sẽ dạy bạn quần vợt nhưng không phải hôm nay. Trời nóng quá.
Chúng ta hãy đi bơi lạnh trên sông.
Đây là phần cuối của phần hai.""",
    },
    {
        "id": 28,
        "title": "Cinema | North | London",
        "icon": "🖥️",
        "file": "PRACTICE FOR EXAM 1 part 1.mp3",
        "en": """Now open your question paper and look at part 1.
You will hear some information about a cinema.
Thank you for calling the North London Arts Cinema Wood Green.
There is no one to answer your call at the moment.
The North London Arts Cinema is open seven days a week,
showing a variety of British and foreign films.
Next week we will show an Italian film called Midnight Meeting.
It is set in Milan in the 1950s.
You can see that film from Monday to Thursday.
It will be on twice a day in the evenings.
That's at 6.45 and 9.15.
The film lasts two hours and 15 minutes.
The tickets are £4, but there is a special student ticket at £2.80 for all our midweek films.
Please bring your student card if you want the cheaper ticket.
The nearest car park to the cinema is in Hoxton Street.
That's H-A-U-X-T-O-N.
It's just five minutes walk from the cinema.
Thank you for calling the North London Arts Cinema.
If you require further information, phone during office hours.
9 a.m. to 4.30 p.m. Monday to Friday.
Now listen again.
Thank you for calling the North London Arts Cinema Wood Green.
There is no one to answer your call at the moment.
The North London Arts Cinema is open seven days a week,
showing a variety of British and foreign films.
Next week we will show an Italian film called Midnight Meeting.
It is set in Milan in the 1950s.
You can see that film from Monday to Thursday.
It will be on twice a day in the evenings.
That's at 6.45 and 9.15.
The film lasts two hours and 15 minutes.
Tickets are £4, but there is a special student ticket at £2.80 for all our midweek films.
Please bring your student card if you want the cheaper ticket.
The nearest car park to the cinema is in Hoxton Street.
That's H-A-U-X-T-O-N.
It's just five minutes walk from the cinema.
Thank you for calling the North London Arts Cinema.
If you require further information, phone during office hours.
9am to 4.30pm, Monday to Friday.""",
        "vi": """Bây giờ hãy mở tờ câu hỏi của bạn và xem phần 1.
Bạn sẽ nghe thấy một số thông tin về một rạp chiếu phim.
Cảm ơn bạn đã gọi đến Rạp chiếu phim nghệ thuật Bắc Luân Đôn Wood Green.
Không có ai trả lời cuộc gọi của bạn vào lúc này.
Rạp chiếu phim nghệ thuật Bắc Luân Đôn mở cửa bảy ngày một tuần,
chiếu nhiều loại phim của Anh và nước ngoài.
Tuần tới chúng tôi sẽ chiếu một bộ phim Ý tên là Cuộc gặp gỡ lúc nửa đêm.
Nó lấy bối cảnh ở Milan vào những năm 1950.
Bạn có thể xem bộ phim đó từ thứ Hai đến thứ Năm.
Nó sẽ diễn ra hai lần một ngày vào buổi tối.
Đó là lúc 6 giờ 45 và 9 giờ 15.
Bộ phim kéo dài hai giờ 15 phút.
Vé là £4, nhưng có một vé đặc biệt dành cho sinh viên là £2,80 cho tất cả các bộ phim giữa tuần của chúng tôi.
Vui lòng mang theo thẻ sinh viên nếu bạn muốn mua vé rẻ hơn.
Bãi đậu xe gần rạp chiếu phim nhất là ở phố Hoxton.
Đó là H-A-U-X-T-O-N.
Nó chỉ cách rạp chiếu phim năm phút đi bộ.
Cảm ơn bạn đã gọi đến Rạp chiếu phim nghệ thuật Bắc Luân Đôn.
Nếu bạn cần thêm thông tin, hãy gọi điện trong giờ hành chính.
9 giờ sáng đến 4 giờ 30 chiều Thứ Hai đến thứ Sáu.
Bây giờ hãy nghe lại.
Cảm ơn bạn đã gọi đến Rạp chiếu phim nghệ thuật Bắc Luân Đôn Wood Green.
Không có ai trả lời cuộc gọi của bạn vào lúc này.
Rạp chiếu phim nghệ thuật Bắc Luân Đôn mở cửa bảy ngày một tuần,
chiếu nhiều loại phim của Anh và nước ngoài.
Tuần tới chúng tôi sẽ chiếu một bộ phim Ý tên là Cuộc gặp gỡ lúc nửa đêm.
Nó lấy bối cảnh ở Milan vào những năm 1950.
Bạn có thể xem bộ phim đó từ thứ Hai đến thứ Năm.
Nó sẽ diễn ra hai lần một ngày vào buổi tối.
Đó là lúc 6 giờ 45 và 9 giờ 15.
Bộ phim kéo dài hai giờ 15 phút.
Vé là £4, nhưng có một vé đặc biệt dành cho sinh viên là £2,80 cho tất cả các bộ phim vào giữa tuần của chúng tôi.
Vui lòng mang theo thẻ sinh viên nếu bạn muốn mua vé rẻ hơn.
Bãi đậu xe gần rạp chiếu phim nhất là ở phố Hoxton.
Đó là H-A-U-X-T-O-N.
Nó chỉ cách rạp chiếu phim năm phút đi bộ.
Cảm ơn bạn đã gọi đến Rạp chiếu phim nghệ thuật Bắc Luân Đôn.
Nếu bạn cần thêm thông tin, hãy gọi điện trong giờ hành chính.
9 giờ sáng đến 4 giờ 30 chiều, từ Thứ Hai đến Thứ Sáu.""",
    },
    {
        "id": 29,
        "title": "Too | Sports | Centre",
        "icon": "🧳",
        "file": "PRACTICE FOR EXAM 1 part 2.mp3",
        "en": """Now look at part 2.
Listen to Sarah talking to a friend about a sports centre.
What is the problem with the different things at the sports centre?
For questions 6 to 10 write a letter A to H next to each thing.
You will hear the conversation twice.
I like your new t-shirt Sarah.
The colours are nice but the problem is it's too big.
I got it from the shop at the sports centre.
I went swimming there because it was a hot day but it was too noisy for me.
There were a lot of people in the pool.
So was it difficult to find a space in the car park there?
Yes. It's not big enough.
Did you go to the cafe?
Yes for a cold drink.
But I didn't stay. The tables and floor weren't clean.
But I hear they have a good football club there.
That's right. My brother wanted to go but it starts too late in the evening for him.
It's a pity because it's not an expensive club.
Can you learn tennis there?
I called about lessons but they cost too much.
I'll teach you tennis but not today. It's too hot.
Let's go for a cold swim in the river.
Now listen again.
I like your new t-shirt Sarah.
The colors are nice but the problem is it's too big.
I got it from the shop at the sports centre.
I went swimming there because it was a hot day but it was too noisy for me.
There were a lot of people in the pool.
So was it difficult to find a space in the car park there?
Yes. It's not big enough.
Did you go to the cafe?
Yes for a cold drink.
But I didn't stay. The tables and floor weren't clean.
Ugh. But I hear they have a good football club there.
That's right. My brother wanted to go but it starts too late in the evening for him.
It's a pity because it's not an expensive club.
Can you learn tennis there?
I called about lessons but they cost too much.
I'll teach you tennis but not today. It's too hot.
Let's go for a cold swim in the river.
This is the end of part two.""",
        "vi": """Bây giờ hãy xem phần 2.
Nghe Sarah nói chuyện với một người bạn về một trung tâm thể thao.
Vấn đề với những điều khác nhau ở trung tâm thể thao là gì?
Đối với các câu hỏi từ 6 đến 10, hãy viết chữ cái từ A đến H bên cạnh mỗi điều.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Tôi thích chiếc áo phông mới của bạn Sarah.
Màu sắc đẹp nhưng vấn đề là nó quá lớn.
Tôi mua nó từ cửa hàng ở trung tâm thể thao.
Tôi đã đi bơi ở đó vì trời nắng nóng nhưng lại quá ồn ào đối với tôi.
Có rất nhiều người trong hồ bơi.
Vậy tìm chỗ đậu xe ở đó có khó không?
Đúng. Nó không đủ lớn.
Bạn đã đến quán cà phê chưa?
Có cho một thức uống lạnh.
Nhưng tôi đã không ở lại. Bàn và sàn không sạch sẽ.
Nhưng tôi nghe nói ở đó có một câu lạc bộ bóng đá rất tốt.
Đúng vậy. Anh trai tôi muốn đi nhưng trời đã quá muộn đối với anh ấy.
Thật đáng tiếc vì đây không phải là một câu lạc bộ đắt tiền.
Bạn có thể học quần vợt ở đó không?
Tôi đã gọi điện về các bài học nhưng chúng đắt quá.
Tôi sẽ dạy bạn quần vợt nhưng không phải hôm nay. Trời nóng quá.
Chúng ta hãy đi bơi lạnh trên sông.
Bây giờ hãy nghe lại.
Tôi thích chiếc áo phông mới của bạn Sarah.
Màu sắc đẹp nhưng vấn đề là nó quá lớn.
Tôi mua nó từ cửa hàng ở trung tâm thể thao.
Tôi đã đi bơi ở đó vì trời nắng nóng nhưng lại quá ồn ào đối với tôi.
Có rất nhiều người trong hồ bơi.
Vậy tìm chỗ đậu xe ở đó có khó không?
Đúng. Nó không đủ lớn.
Bạn đã đến quán cà phê chưa?
Có cho một thức uống lạnh.
Nhưng tôi đã không ở lại. Bàn và sàn không sạch sẽ.
Ờ. Nhưng tôi nghe nói ở đó có một câu lạc bộ bóng đá rất tốt.
Đúng vậy. Anh trai tôi muốn đi nhưng trời đã quá muộn đối với anh ấy.
Thật đáng tiếc vì đây không phải là một câu lạc bộ đắt tiền.
Bạn có thể học quần vợt ở đó không?
Tôi đã gọi điện về các bài học nhưng chúng đắt quá.
Tôi sẽ dạy bạn quần vợt nhưng không phải hôm nay. Trời nóng quá.
Chúng ta hãy đi bơi lạnh trên sông.
Đây là phần cuối của phần hai.""",
    },
    {
        "id": 30,
        "title": "Man | Questions | Through",
        "icon": "🎁",
        "file": "PRACTICE FOR EXAM 1 part 3.mp3",
        "en": """Part 3.
Listen and choose the correct answer.
Questions 1 through 3 refer to the following conversation.
Excuse me? Haven't we met before?
Yes, I used to work at Evans Department Store.
That's right. You sold shoes there.
Yes, but now I have my own store.
1. Which sentence is true?
2. Where did the man and woman meet first?
3. What did the man use to do?
Questions 4 through 6 refer to the following conversation.
I'm back. Sorry, I'm late.
What took you so long? You missed an appointment with Eric.
I know, but the traffic was really bad.
Well, he wants you to call him. He seemed a little angry.
4. Which sentence is true?
5. Why was the man late?
6. What will the man probably do next?
5. Now listen again.
Questions 1 through 3 refer to the following conversation.
Excuse me? Haven't we met before?
Yes, I used to work at Evans Department Store.
That's right. You sold shoes there.
Yes, but now I have my own store.
1. Which sentence is true?
2. Where did the man and woman meet first?
3. What did the man use to do?
Questions 4 through 6 refer to the following conversation.
I'm back. Sorry, I'm late.
What took you so long? You missed an appointment with Eric.
I know, but the traffic was really bad.
Well, he wants you to call him. He seemed a little angry.
4. Which sentence is true?
5. Why was the man late?
6. What will the man probably do next?""",
        "vi": """Phần 3.
Nghe và chọn câu trả lời đúng.
Câu hỏi từ 1 đến 3 đề cập đến cuộc trò chuyện sau đây.
Xin lỗi? Chúng ta chưa gặp nhau bao giờ à?
Có, tôi từng làm việc ở Cửa hàng bách hóa Evans.
Đúng vậy. Bạn bán giày ở đó.
Có, nhưng bây giờ tôi có cửa hàng của riêng mình.
1. Câu nào đúng?
2. Người đàn ông và người phụ nữ gặp nhau lần đầu tiên ở đâu?
3. Người đàn ông đó đã từng làm gì?
Câu hỏi từ 4 đến 6 đề cập đến cuộc trò chuyện sau đây.
Tôi đã trở lại. Xin lỗi, tôi đến muộn.
Điều gì khiến bạn mất nhiều thời gian thế? Bạn đã lỡ cuộc hẹn với Eric.
Tôi biết, nhưng giao thông thực sự rất tệ.
À, anh ấy muốn bạn gọi cho anh ấy. Anh ấy có vẻ hơi tức giận.
4. Câu nào đúng?
5. Tại sao người đàn ông đó lại đến muộn?
6. Người đàn ông có thể sẽ làm gì tiếp theo?
5. Bây giờ hãy nghe lại.
Câu hỏi từ 1 đến 3 đề cập đến cuộc trò chuyện sau đây.
Xin lỗi? Chúng ta chưa gặp nhau bao giờ à?
Có, tôi từng làm việc ở Cửa hàng bách hóa Evans.
Đúng vậy. Bạn bán giày ở đó.
Có, nhưng bây giờ tôi có cửa hàng của riêng mình.
1. Câu nào đúng?
2. Người đàn ông và người phụ nữ gặp nhau lần đầu tiên ở đâu?
3. Người đàn ông đó đã từng làm gì?
Câu hỏi từ 4 đến 6 đề cập đến cuộc trò chuyện sau đây.
Tôi đã trở lại. Xin lỗi, tôi đến muộn.
Điều gì khiến bạn mất nhiều thời gian thế? Bạn đã lỡ cuộc hẹn với Eric.
Tôi biết, nhưng giao thông thực sự rất tệ.
À, anh ấy muốn bạn gọi cho anh ấy. Anh ấy có vẻ hơi tức giận.
4. Câu nào đúng?
5. Tại sao người đàn ông đó lại đến muộn?
6. Người đàn ông có thể sẽ làm gì tiếp theo?""",
    },
    {
        "id": 31,
        "title": "Class | Now | Friend",
        "icon": "👟",
        "file": "PRACTICE FOR EXAM 1 part 4.mp3",
        "en": """Now look at part four.
You will hear a man asking for information about the Westwood English school.
Listen and complete questions 16 to 20.
You will hear the conversation twice.
Westwood English school?
Hello. I want to ask about evening classes please.
Yes, they're on Thursdays, but this term will finish at the end of August.
We'll start again on the 22nd of September, but you can book your place now.
It's for a Chinese friend. He wants an easy class.
Well, there's a two hour class for beginners.
My friend would like something shorter.
Well, we have a 50 minute speaking class. That would be good for him.
The teacher is Miss Jarvis. That's J-A-R-V-I-S.
The student's all like her.
How much does that class cost?
It's £7.50 per class.
Or if you pay for all 12 classes now, it's only £78.
It's cheaper that way.
Right.
Can your friend come to the school soon and book his place?
The address is 223 Fitzroy Square.
Is that in the centre of town?
Well, it's about 20 minutes walk from the station.
We're just by the bookshop.
Right. Thank you.
Goodbye.
Now listen again.
Westwood English school?
Hello. I want to ask about evening classes, please.
Yes. They're on Thursdays.
But this term will finish at the end of August.
We'll start again on the 22nd of September.
But you can book your place now.
It's for a Chinese friend. He wants an easy class.
Well, there's a two hour class for beginners.
My friend would like something shorter.
Well, we have a 50 minute speaking class.
That would be good for him.
The teacher is Miss Jarvis.
That's J-A-R-V-I-S.
The students all like her.
How much does that class cost?
It's £7.50 per class.
Or if you pay for all 12 classes now, it's only £78.
It's cheaper that way.
Right.
Can your friend come to the school soon and book his place?
The address is 223 Fitzroy Square.
Is that in the centre of town?
Well, it's about 20 minutes walk from the station.
We're just by the book shop.
Right. Thank you.
Goodbye.
This is the end of part four.
Thank you.""",
        "vi": """Bây giờ hãy xem phần bốn.
Bạn sẽ nghe thấy một người đàn ông hỏi thông tin về trường Anh ngữ Westwood.
Nghe và hoàn thành các câu hỏi từ 16 đến 20.
Bạn sẽ nghe cuộc trò chuyện hai lần.
Trường Anh ngữ Westwood?
Xin chào. Mình muốn hỏi về lớp học buổi tối.
Vâng, họ tổ chức vào thứ Năm, nhưng học kỳ này sẽ kết thúc vào cuối tháng Tám.
Chúng tôi sẽ bắt đầu lại vào ngày 22 tháng 9, nhưng bạn có thể đặt chỗ ngay bây giờ.
Nó dành cho một người bạn Trung Quốc. Anh ấy muốn một lớp học dễ dàng.
Vâng, có một lớp học kéo dài hai giờ dành cho người mới bắt đầu.
Bạn tôi muốn cái gì đó ngắn hơn.
À, chúng ta có một lớp học nói 50 phút. Điều đó sẽ tốt cho anh ấy.
Giáo viên là cô Jarvis. Đó là J-A-R-V-I-S.
Học sinh nào cũng giống cô ấy.
Lớp học đó có giá bao nhiêu?
Đó là £ 7,50 mỗi lớp.
Hoặc nếu bây giờ bạn trả tiền cho tất cả 12 lớp thì chỉ còn £78.
Cách đó rẻ hơn.
Phải.
Bạn của bạn có thể đến trường sớm và đặt chỗ được không?
Địa chỉ là 223 Quảng trường Fitzroy.
Đó có phải là ở trung tâm thị trấn không?
À, cách ga khoảng 20 phút đi bộ.
Chúng tôi đang ở cạnh hiệu sách.
Phải. Cảm ơn.
Tạm biệt.
Bây giờ hãy nghe lại.
Trường Anh ngữ Westwood?
Xin chào. Mình muốn hỏi về lớp học buổi tối.
Đúng. Họ đang vào thứ Năm.
Nhưng học kỳ này sẽ kết thúc vào cuối tháng 8.
Chúng ta sẽ bắt đầu lại vào ngày 22 tháng 9.
Nhưng bạn có thể đặt chỗ ngay bây giờ.
Nó dành cho một người bạn Trung Quốc. Anh ấy muốn một lớp học dễ dàng.
Vâng, có một lớp học kéo dài hai giờ dành cho người mới bắt đầu.
Bạn tôi muốn cái gì đó ngắn hơn.
À, chúng ta có một lớp học nói 50 phút.
Điều đó sẽ tốt cho anh ấy.
Giáo viên là cô Jarvis.
Đó là J-A-R-V-I-S.
Các sinh viên đều thích cô ấy.
Lớp học đó có giá bao nhiêu?
Đó là £ 7,50 mỗi lớp.
Hoặc nếu bây giờ bạn trả tiền cho tất cả 12 lớp thì chỉ còn £78.
Cách đó rẻ hơn.
Phải.
Bạn của bạn có thể đến trường sớm và đặt chỗ được không?
Địa chỉ là 223 Quảng trường Fitzroy.
Đó có phải là ở trung tâm thị trấn không?
À, cách ga khoảng 20 phút đi bộ.
Chúng tôi đang ở gần hiệu sách.
Phải. Cảm ơn.
Tạm biệt.
Đây là phần cuối của phần bốn.
Cảm ơn.""",
    },
    {
        "id": 32,
        "title": "London | Concert | Information",
        "icon": "🏥",
        "file": "PRACTICE FOR EXAM 2 part 1.mp3",
        "en": """Now open your question paper and look at part 1.
You will hear some information about a pop concert.
You will hear the information twice.
You are listening to Radio South.
Here is some information about a pop concert.
The group Red River will come to London soon.
They will be in London from the 28th of October to the 2nd of November.
After that they will be in Oxford from the 4th of November until the 9th.
Tickets are quite expensive.
They cost 37 pounds each, but half of that money will go to a children's hospital.
This will sell quickly for this famous band so book early.
To book a ticket for a London concert, telephone 283 0065 between 10am and 10pm.
Have a credit card number ready.
The London concerts will be in South Bank Hall.
It's very easy to find.
The best way to get there is to take the train.
The concert hall is in Trinity Street.
That's T-R-I-N-I-T-Y Street.
See you there.
For classical music lovers.
Now listen again.
You are listening to Radio South.
There is some information about a pop concert.
The group Red River will come to London soon.
They will be in London from the 28th of October to the 2nd of November.
After that they will be in Oxford from the 4th of November until the 9th.
Tickets are quite expensive.
They cost 37 pounds each, but half of that money will go to a children's hospital.
This will sell quickly for this famous band so book early.
To book a ticket for a London concert, telephone 283 0065 between 10am and 10pm.
Have a credit card number ready.
The London concerts will be in South Bank Hall.
It's very easy to find.
The best way to get there is to take the train.
The concert hall is in Trinity Street.
That's T-R-I-N-I-T-Y Street.
See you there.
For classical music lovers.""",
        "vi": """Bây giờ hãy mở tờ câu hỏi của bạn và xem phần 1.
Bạn sẽ nghe một số thông tin về một buổi hòa nhạc pop.
Bạn sẽ nghe thông tin hai lần.
Bạn đang nghe Đài phát thanh miền Nam.
Dưới đây là một số thông tin về một buổi hòa nhạc pop.
Nhóm Red River sẽ sớm đến London.
Họ sẽ ở London từ ngày 28 tháng 10 đến ngày 2 tháng 11.
Sau đó họ sẽ ở Oxford từ ngày 4 tháng 11 đến ngày 9 tháng 11.
Vé khá đắt.
Mỗi chiếc có giá 37 bảng, nhưng một nửa số tiền đó sẽ được chuyển đến bệnh viện nhi.
Điều này sẽ bán nhanh chóng cho ban nhạc nổi tiếng này vì vậy hãy đặt sớm.
Để đặt vé cho buổi hòa nhạc ở London, hãy gọi số 283 0065 trong khoảng thời gian từ 10 giờ sáng đến 10 giờ tối.
Chuẩn bị sẵn số thẻ tín dụng.
Buổi hòa nhạc ở London sẽ diễn ra ở South Bank Hall.
Nó rất dễ tìm thấy.
Cách tốt nhất để đến đó là đi tàu.
Phòng hòa nhạc nằm ở phố Trinity.
Đó là đường T-R-I-N-I-T-Y.
Hẹn gặp bạn ở đó.
Dành cho những người yêu thích âm nhạc cổ điển.
Bây giờ hãy nghe lại.
Bạn đang nghe Đài phát thanh miền Nam.
Có một số thông tin về một buổi hòa nhạc pop.
Nhóm Red River sẽ sớm đến London.
Họ sẽ ở London từ ngày 28 tháng 10 đến ngày 2 tháng 11.
Sau đó họ sẽ ở Oxford từ ngày 4 tháng 11 đến ngày 9 tháng 11.
Vé khá đắt.
Mỗi chiếc có giá 37 bảng, nhưng một nửa số tiền đó sẽ được chuyển đến bệnh viện nhi.
Điều này sẽ bán nhanh chóng cho ban nhạc nổi tiếng này vì vậy hãy đặt sớm.
Để đặt vé cho buổi hòa nhạc ở London, hãy gọi số 283 0065 trong khoảng thời gian từ 10 giờ sáng đến 10 giờ tối.
Chuẩn bị sẵn số thẻ tín dụng.
Buổi hòa nhạc ở London sẽ diễn ra ở South Bank Hall.
Nó rất dễ tìm thấy.
Cách tốt nhất để đến đó là đi tàu.
Phòng hòa nhạc nằm ở phố Trinity.
Đó là đường T-R-I-N-I-T-Y.
Hẹn gặp bạn ở đó.
Dành cho những người yêu thích âm nhạc cổ điển.""",
    },
    {
        "id": 33,
        "title": "Think | Does | Questions",
        "icon": "🛋️",
        "file": "PRACTICE FOR EXAM 2 part 3.mp3",
        "en": """Part 3.
Listen and choose the correct answer.
Questions 1 through 3 refer to the following conversation.
Are we going to buy the green curtains or the yellow curtains for the main conference room?
The manager decided to go for green.
I think it's a good choice.
Yes, I hope it will help reduce stress during meetings.
1. What are the men and women discussing?
2. What color did the manager select?
3. Why does the man think it is a good idea?
Questions 4 through 6 refer to the following conversation.
What's the matter?
I can't find my glasses.
They are probably on your desk.
No, oh yes, I remember leaving them in my car.
4. What is the woman doing?
5. Where does the man think the glasses are?
6. What does the woman remember?
5. Now listen again.
Questions 1 through 3 refer to the following conversation.
Are we going to buy the green curtains or the yellow curtains for the main conference room?
The manager decided to go for green.
I think it's a good choice.
Yes, I hope it will help reduce stress during meetings.
1. What are the men and women discussing?
2. What color did the manager select?
3. Why does the man think it is a good idea?
Questions 4 through 6 refer to the following conversation.
What's the matter?
I can't find my glasses.
They are probably on your desk.
No, oh yes, I remember leaving them in my car.
4. What is the woman doing?
5. Where does the man think the glasses are?
6. What does the woman remember?""",
        "vi": """Phần 3.
Nghe và chọn câu trả lời đúng.
Câu hỏi từ 1 đến 3 đề cập đến cuộc trò chuyện sau đây.
Chúng ta sẽ mua rèm màu xanh lá cây hay rèm màu vàng cho phòng họp chính?
Người quản lý quyết định chọn màu xanh lá cây.
Tôi nghĩ đó là một lựa chọn tốt.
Vâng, tôi hy vọng nó sẽ giúp giảm bớt căng thẳng trong các cuộc họp.
1. Nam nữ đang thảo luận về vấn đề gì?
2. Người quản lý đã chọn màu gì?
3. Tại sao người đàn ông nghĩ đó là một ý tưởng hay?
Câu hỏi từ 4 đến 6 đề cập đến cuộc trò chuyện sau đây.
Có chuyện gì vậy?
Tôi không thể tìm thấy kính của tôi.
Có lẽ chúng đang ở trên bàn làm việc của bạn.
Không, ồ vâng, tôi nhớ đã để chúng trong xe của mình.
4. Người phụ nữ đang làm gì?
5. Người đàn ông nghĩ chiếc kính ở đâu?
6. Người phụ nữ nhớ gì?
5. Bây giờ hãy nghe lại.
Câu hỏi từ 1 đến 3 đề cập đến cuộc trò chuyện sau đây.
Chúng ta sẽ mua rèm màu xanh lá cây hay rèm màu vàng cho phòng họp chính?
Người quản lý quyết định chọn màu xanh lá cây.
Tôi nghĩ đó là một lựa chọn tốt.
Vâng, tôi hy vọng nó sẽ giúp giảm bớt căng thẳng trong các cuộc họp.
1. Nam nữ đang thảo luận về vấn đề gì?
2. Người quản lý đã chọn màu gì?
3. Tại sao người đàn ông nghĩ đó là một ý tưởng hay?
Câu hỏi từ 4 đến 6 đề cập đến cuộc trò chuyện sau đây.
Có chuyện gì vậy?
Tôi không thể tìm thấy kính của tôi.
Có lẽ chúng đang ở trên bàn làm việc của bạn.
Không, ồ vâng, tôi nhớ đã để chúng trong xe của mình.
4. Người phụ nữ đang làm gì?
5. Where does the man think the glasses are?
6. What does the woman remember?""",
    },
    {
        "id": 34,
        "title": "Going | Store | Where",
        "icon": "💎",
        "file": "Q1.mp3",
        "en": """Where is he going?
A.
She's going to the store.
B.
I'm going to the store.
C.
He's going to the store.""",
        "vi": """Anh ấy đang đi đâu vậy?
A.
Cô ấy đang đi đến cửa hàng.
B.
Tôi đang đi đến cửa hàng.
C.
Anh ấy đang đi đến cửa hàng.""",
    },
    {
        "id": 35,
        "title": "Listen | Choose | Correct",
        "icon": "🎵",
        "file": "Q10.mp3",
        "en": """Listen and choose the correct answer.
Is the window open?
A.
No, it doesn't.
B.
Yes, it does.
C.
No, it isn't.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Cửa sổ có mở không?
A.
Không, nó không.
B.
Vâng, nó có.
C.
Không, không phải vậy.""",
    },
    {
        "id": 36,
        "title": "Listen | Choose | Correct",
        "icon": "🎸",
        "file": "Q11.mp3",
        "en": """Listen and choose the correct answer.
How have you been lately?
A. I'm sorry I'm late.
B. Great.
C. Two hours.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Gần đây bạn thế nào?
A. Tôi xin lỗi tôi đến muộn.
B. Tuyệt vời.
C. Hai giờ.""",
    },
    {
        "id": 37,
        "title": "Listen | Choose | Correct",
        "icon": "🎹",
        "file": "Q13.mp3",
        "en": """Listen and choose the correct answer.
When did the show start?
A. I don't have time right now.
B. 20 minutes ago.
C. In a couple of hours.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Buổi diễn bắt đầu khi nào?
A. Bây giờ tôi không có thời gian.
B. 20 phút trước.
C. Trong vài giờ nữa.""",
    },
    {
        "id": 38,
        "title": "Turn | Phew | Hot",
        "icon": "🌤️",
        "file": "Q2.mp3",
        "en": """Phew, it's hot in here.
A. I'll turn on the fan.
B. I'll turn on the heat.
C. I'll turn on the lights.""",
        "vi": """Phù, ở đây nóng quá.
A. Tôi sẽ bật quạt.
B. Tôi sẽ bật lửa lên.
C. Tôi sẽ bật đèn lên.""",
    },
    {
        "id": 39,
        "title": "Listen | Choose | Correct",
        "icon": "🎧",
        "file": "Q20.mp3",
        "en": """Listen and choose the correct answer.
Do you like chocolate ice cream?
A.
No, I can't.
B.
Yes, I do.
C.
Yes, I can.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Bạn có thích kem sô cô la không?
A.
Không, tôi không thể.
B.
Vâng, tôi biết.
C.
Vâng, tôi có thể.""",
    },
    {
        "id": 40,
        "title": "Because | Subway | Ride",
        "icon": "📈",
        "file": "Q21-23.mp3",
        "en": """Listen and choose the best answer to each question.
I usually ride my bicycle to work.
It's much faster than taking the bus because I can take a shortcut through the park.
It takes about 20 minutes in total.
The subway is even slower because it is a 15 minute walk from my house to the subway station.
Then the subway ride is another 20 minutes.
In the winter though, I have to take the bus because of the weather.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Tôi thường đi xe đạp đi làm.
Nó nhanh hơn nhiều so với đi xe buýt vì tôi có thể đi đường tắt qua công viên.
Tổng cộng mất khoảng 20 phút.
Tàu điện ngầm thậm chí còn chậm hơn vì từ nhà tôi đến ga tàu điện ngầm mất 15 phút đi bộ.
Sau đó đi tàu điện ngầm thêm 20 phút nữa.
Tuy nhiên, vào mùa đông, tôi phải đi xe buýt vì thời tiết.""",
    },
    {
        "id": 41,
        "title": "Doctor | Want | Very",
        "icon": "🛁",
        "file": "Q24-26.mp3",
        "en": """Listen and choose the best answer to each question.
After university, I want to be a doctor.
Doctors have very important jobs.
When I was younger, my mom was very sick.
She stayed in the hospital for one month.
I was so happy when she returned home.
It really made me want to be a doctor so that I could help sick people too.
It is hard work to become a doctor, but I'm going to study hard.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Sau đại học, tôi muốn trở thành bác sĩ.
Bác sĩ có công việc rất quan trọng.
Khi tôi còn nhỏ, mẹ tôi bị bệnh nặng.
Cô ở lại bệnh viện một tháng.
Tôi rất vui khi cô ấy trở về nhà.
Nó thực sự khiến tôi muốn trở thành bác sĩ để có thể giúp đỡ những người bệnh.
Trở thành bác sĩ thật vất vả nhưng tôi sẽ học tập chăm chỉ.""",
    },
    {
        "id": 42,
        "title": "Tickets | Constant | Hall",
        "icon": "💰",
        "file": "Q27-29.mp3",
        "en": """Listen and choose the best answer to each question.
Due to problems with the lighting, the constant has to be postponed until Friday the 22nd.
The constant will also be moved from Hall A to the larger Hall C. A bigger venue means
a further 500 tickets will now be available twice the original number.
Most of the extra tickets, tickets will now be priced at the lower cost of $20.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Do vấn đề về ánh sáng nên buổi lễ phải hoãn lại cho đến thứ Sáu ngày 22.
Hằng số cũng sẽ được chuyển từ Hội trường A đến Hội trường C lớn hơn. Địa điểm lớn hơn có nghĩa là
500 vé nữa bây giờ sẽ có sẵn gấp đôi số lượng ban đầu.
Hầu hết các vé bổ sung hiện nay sẽ có giá thấp hơn là 20 USD.""",
    },
    {
        "id": 43,
        "title": "Watching | Movie | Listen",
        "icon": "🎤",
        "file": "Q3.mp3",
        "en": """Listen and choose the correct answer.
3. What are you watching?
A. You're watching a movie.
B. I'm watching a movie.
C. I'll watch a movie.""",
        "vi": """Nghe và chọn câu trả lời đúng.
3. Bạn đang xem gì?
A. Bạn đang xem phim.
B. Tôi đang xem phim.
C. Tôi sẽ xem một bộ phim.""",
    },
    {
        "id": 44,
        "title": "Spanish | Listen | Choose",
        "icon": "✏️",
        "file": "Q30-32.mp3",
        "en": """Listen and choose the best answer to each question.
This year at University, I am studying three languages.
English is the most difficult.
French and Spanish are both quite easy.
I have lots of chances to practice Spanish because I live with my Mexican friend.
I am getting used to speaking Spanish outside of class.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Năm nay tại trường Đại học, tôi đang học ba ngôn ngữ.
Tiếng Anh là khó nhất.
Tiếng Pháp và tiếng Tây Ban Nha đều khá dễ dàng.
Tôi có nhiều cơ hội thực hành tiếng Tây Ban Nha vì tôi sống với người bạn Mexico.
Tôi đang dần quen với việc nói tiếng Tây Ban Nha bên ngoài lớp học.""",
    },
    {
        "id": 45,
        "title": "Flight | Listen | Choose",
        "icon": "💊",
        "file": "Q36-38.mp3",
        "en": """Listen and choose the best answer to each question.
Attention all passengers on flight KL162 from Spain to Ireland.
This flight has been delayed due to bad weather.
The flight will now be leaving at 7.15pm from gate 22A.
We apologise for any inconvenience.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Tất cả hành khách trên chuyến bay KL162 từ Tây Ban Nha đến Ireland chú ý.
Chuyến bay này đã bị trì hoãn do thời tiết xấu.
Chuyến bay sẽ khởi hành lúc 19h15 từ cổng 22A.
Chúng tôi xin lỗi vì bất kỳ sự bất tiện nào.""",
    },
    {
        "id": 46,
        "title": "Did | Listen | Choose",
        "icon": "🎷",
        "file": "Q4.mp3",
        "en": """Listen and choose the correct answer.
4.
How did you do that?
A. I did it.
B. It's easy. I'll show you.
C. No, you didn't.""",
        "vi": """Nghe và chọn câu trả lời đúng.
4.
Bạn đã làm điều đó như thế nào?
A. Tôi đã làm được.
B. Thật dễ dàng. Tôi sẽ chỉ cho bạn.
C. Không, bạn đã không làm thế.""",
    },
    {
        "id": 47,
        "title": "Korean | Here | Listen",
        "icon": "💉",
        "file": "Q45-47.mp3",
        "en": """Listen and choose the best answer to each question.
This is my friend Pablo from Spain.
He came here six months ago.
He is here studying Korean and economics at Seoul National University.
He speaks Korean very well and he really enjoys Korean food.
He will be going back to Madrid next February.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Đây là bạn tôi Pablo đến từ Tây Ban Nha.
Anh ấy đến đây sáu tháng trước.
Anh ấy đang học tiếng Hàn và kinh tế tại Đại học Quốc gia Seoul.
Anh ấy nói tiếng Hàn rất tốt và rất thích đồ ăn Hàn Quốc.
Anh ấy sẽ trở lại Madrid vào tháng 2 tới.""",
    },
    {
        "id": 48,
        "title": "Listen | Choose | Best",
        "icon": "🎺",
        "file": "Q48-50.mp3",
        "en": """Listen and choose the best answer to each question.
Questions 4-6 refer to the following announcement.
Could the owner of a green in Red Dayson, Santa Lucia registration number ST-4571
please come to the parking lot immediately?
Your car is blocking the entrance.
A delivery truck is unable to enter and this is causing a traffic jam in the street outside the store.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Câu hỏi 4-6 đề cập đến thông báo sau.
Liệu chủ nhân của bãi cỏ xanh ở Red Dayson, Santa Lucia có số đăng ký ST-4571
xin vui lòng đến bãi đậu xe ngay lập tức?
Xe của bạn đang chặn lối vào.
Xe giao hàng không thể vào được khiến đường phố bên ngoài cửa hàng bị ùn tắc.""",
    },
    {
        "id": 49,
        "title": "Korean | Here | Listen",
        "icon": "🩺",
        "file": "Q51-53.mp3",
        "en": """Listen and choose the best answer to each question.
This is my friend Pablo from Spain.
He came here six months ago.
He is here studying Korean and economics at Seoul National University.
He speaks Korean very well and he really enjoys Korean food.
He will be going back to Madrid next February.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Đây là bạn tôi Pablo đến từ Tây Ban Nha.
Anh ấy đến đây sáu tháng trước.
Anh ấy đang học tiếng Hàn và kinh tế tại Đại học Quốc gia Seoul.
Anh ấy nói tiếng Hàn rất tốt và rất thích đồ ăn Hàn Quốc.
Anh ấy sẽ trở lại Madrid vào tháng 2 tới.""",
    },
    {
        "id": 50,
        "title": "Listen | Choose | Best",
        "icon": "🌧️",
        "file": "Q54-56.mp3",
        "en": """Listen and choose the best answer to each question.
Could the owner of a green and red Daysung Santa Lucia registration number ST-4571 please
come to the parking lot immediately?
Your car is blocking the entrance.
A delivery truck is unable to enter and this is causing a traffic jam in the street outside
the store.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Xin chủ nhân chiếc xe Daysung Santa Lucia số đăng ký ST-4571 màu xanh và đỏ
đến bãi đậu xe ngay lập tức?
Xe của bạn đang chặn lối vào.
Xe giao hàng không thể vào được khiến đường phố bên ngoài ùn tắc
cửa hàng.""",
    },
    {
        "id": 51,
        "title": "Learning | Korean | Students",
        "icon": "🏫",
        "file": "Q57-59.mp3",
        "en": """Listen and choose the best answer to each question.
Are you interested in learning Korean?
If so, come to our free classes at Hondo English Institute.
Here, learning is fun.
Students learn Korean with people from many different countries.
Students begin at 12 o'clock on Saturdays and 2 o'clock on Sundays.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Bạn có thích học tiếng Hàn không?
Nếu vậy, hãy đến với các lớp học miễn phí của chúng tôi tại Học viện Anh ngữ Hondo.
Ở đây học tập rất vui.
Học sinh học tiếng Hàn với mọi người đến từ nhiều quốc gia khác nhau.
Học sinh bắt đầu vào lúc 12 giờ ngày thứ bảy và 2 giờ ngày chủ nhật.""",
    },
    {
        "id": 52,
        "title": "Listen | Choose | Correct",
        "icon": "💡",
        "file": "Q6.mp3",
        "en": """Listen and choose the correct answer.
Who were you talking to?
A.
To the store.
B.
To buy some ice cream.
C.
To a friend.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Bạn đang nói chuyện với ai vậy?
A.
Đến cửa hàng.
B.
Để mua một ít kem.
C.
Gửi một người bạn.""",
    },
    {
        "id": 53,
        "title": "Zoo | Listen | Choose",
        "icon": "🗂️",
        "file": "Q60-62.mp3",
        "en": """Listen and choose the best answer to each question.
I have been working at the zoo for over 20 years now.
Every day I have to feed the elephants and make sure that they have enough water.
On my break I like to walk around the zoo and look at the other animals.
The hippo is my second favorite animal after the elephant.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Tôi đã làm việc ở sở thú được hơn 20 năm rồi.
Hàng ngày tôi phải cho voi ăn và đảm bảo chúng có đủ nước.
Vào giờ nghỉ, tôi thích đi dạo quanh sở thú và ngắm nhìn các loài động vật khác.
Hà mã là loài động vật tôi yêu thích thứ hai sau voi.""",
    },
    {
        "id": 54,
        "title": "Clock | Get | Work",
        "icon": "👔",
        "file": "Q63-65.mp3",
        "en": """Listen and choose the best answer to each question.
My schedule is as busy as my friend's schedules. Usually I wake up at 7 o'clock, I get on a bus
at 8 o'clock, and arrive at work at 9. After I get off work at about 6 o'clock, I go
shopping or walk through the park with my wife. Sometimes, when I want a quiet evening,
I just stay at home and watch TV.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Lịch trình của tôi cũng bận rộn như lịch trình của bạn tôi. Thường thì tôi thức dậy lúc 7 giờ và lên xe buýt
lúc 8 giờ và đến nơi làm việc lúc 9 giờ. Sau khi tan sở vào khoảng 6 giờ, tôi đi
đi mua sắm hoặc đi dạo công viên với vợ tôi. Đôi khi, khi tôi muốn một buổi tối yên tĩnh,
Tôi chỉ ở nhà và xem TV.""",
    },
    {
        "id": 55,
        "title": "Hop | Down | Bunny",
        "icon": "🎒",
        "file": "Q66-68.mp3",
        "en": """Listen and choose the best answer to each question.
Hop on down to bunny motors for a huge sales event.
We have the fastest and most expensive cars on the market.
But you can now save up to 50% on the purchase of a new automobile.
Want to see him richer and be smarter than all your neighbors?
Then hop on down to bunny motors today.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Nhảy xuống động cơ thỏ cho một sự kiện bán hàng lớn.
Chúng tôi có những chiếc xe nhanh nhất và đắt nhất trên thị trường.
Nhưng giờ đây bạn có thể tiết kiệm tới 50% khi mua một chiếc ô tô mới.
Bạn muốn thấy anh ta giàu có hơn và thông minh hơn tất cả những người hàng xóm của bạn?
Sau đó hãy chuyển sang động cơ thỏ ngay hôm nay.""",
    },
    {
        "id": 56,
        "title": "Opponent | Listen | Choose",
        "icon": "🚑",
        "file": "Q69-71.mp3",
        "en": """Listen and choose the best answer to each question.
I have been studying judo for over 10 years.
During my last competition, one opponent pulled my shoulder out of its socket.
Despite the pain, I was able to throw my opponent to the ground because I really didn't
want to lose.
The referee raised my hand in victory.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Tôi đã học judo được hơn 10 năm.
Trong cuộc thi gần đây nhất của tôi, một đối thủ đã kéo vai tôi ra khỏi ổ cắm của nó.
Dù đau đớn nhưng tôi vẫn có thể ném đối thủ xuống đất vì tôi thực sự không làm vậy.
muốn thua.
Trọng tài đã giơ tay biểu thị chiến thắng của tôi.""",
    },
    {
        "id": 57,
        "title": "Tired | Listen | Choose",
        "icon": "🌟",
        "file": "Q7.mp3",
        "en": """Listen and choose the correct answer.
Why did you leave early?
A. I was tired.
B. She is more tired.
C. You are tired.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Tại sao bạn lại rời đi sớm?
A. Tôi mệt mỏi.
B. Cô ấy mệt mỏi hơn.
C. Bạn mệt mỏi.""",
    },
    {
        "id": 58,
        "title": "Choose | Listen | Best",
        "icon": "📁",
        "file": "Q72-74.mp3",
        "en": """Listen and choose the best answer to each question.
Over the past few years, I've had many jobs in the service industry.
My duties included watering plants, sweeping floors, and serving customers in a restaurant.
So even though I look very young, I have a lot of experience.
If you choose to hire me, I can be available to start work as soon as tomorrow morning.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Trong vài năm qua, tôi đã làm được nhiều việc trong ngành dịch vụ.
Nhiệm vụ của tôi bao gồm tưới cây, quét sàn và phục vụ khách hàng trong nhà hàng.
Vì vậy, dù trông tôi còn rất trẻ nhưng tôi có rất nhiều kinh nghiệm.
Nếu bạn chọn thuê tôi, tôi có thể sẵn sàng bắt đầu công việc ngay vào sáng mai.""",
    },
    {
        "id": 59,
        "title": "Yoga | Answer | Relax",
        "icon": "✨",
        "file": "Q75-77.mp3",
        "en": """Listen and choose the best answer to each question.
Do you find it difficult to relax?
Are you always stressed?
If so, the answer to your problem is yoga.
Yoga can help your body relax and give you a lot more energy.
Check the Rama Yoga Center at 311-4265 for more information.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Bạn có thấy khó thư giãn không?
Bạn luôn bị căng thẳng?
Nếu vậy, câu trả lời cho vấn đề của bạn chính là yoga.
Yoga có thể giúp cơ thể bạn thư giãn và cung cấp cho bạn nhiều năng lượng hơn.
Hãy kiểm tra Trung tâm Yoga Rama theo số 311-4265 để biết thêm thông tin.""",
    },
    {
        "id": 60,
        "title": "Would | Went | Vacation",
        "icon": "📌",
        "file": "Q78-80.mp3",
        "en": """Listen and choose the best answer to each question.
Two years ago, I went on vacation to Canada. I really enjoyed it.
I went for walks in the mountains by myself. Then I would meet my friends and we would have dinner together.
I would love to go back on another vacation.""",
        "vi": """Nghe và chọn câu trả lời đúng nhất cho mỗi câu hỏi.
Hai năm trước, tôi đi nghỉ ở Canada. Tôi thực sự rất thích nó.
Tôi đã tự mình đi dạo trên núi. Sau đó tôi sẽ gặp bạn bè và chúng tôi sẽ ăn tối cùng nhau.
Tôi rất muốn quay lại vào một kỳ nghỉ khác.""",
    },
    {
        "id": 61,
        "title": "Listen | Choose | Correct",
        "icon": "🧩",
        "file": "Q8.mp3",
        "en": """Listen and choose the correct answer.
When is your brother's birthday?
A. Last year.
B. Next Tuesday.
C. On time.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Sinh nhật của anh trai bạn là khi nào?
A. Năm ngoái.
B. Thứ Ba tới.
C. Đúng giờ.""",
    },
    {
        "id": 62,
        "title": "Office | Much | One",
        "icon": "📊",
        "file": "Q87-89.mp3",
        "en": """Is that the new computer the office bought for you?
It looks pretty nice.
I hadn't realized they were going to buy laptops.
Yes, I love it.
It's so much faster than my old one, and I can just take it home with me if I want to
get something finished instead of staying late at the office.
I've only had it a week, but it has already made my life so much easier.
Great.
I'm on the list to get one too.
I can't wait to start using it.
Number 41.""",
        "vi": """Đó có phải là chiếc máy tính mới mà văn phòng mua cho bạn không?
Nó trông khá đẹp.
Tôi đã không nhận ra họ sẽ mua máy tính xách tay.
Vâng, tôi thích nó.
Nó nhanh hơn rất nhiều so với cái cũ của tôi và tôi có thể mang nó về nhà nếu muốn
hoàn thành việc gì đó thay vì ở lại văn phòng muộn.
Tôi chỉ mới dùng được một tuần nhưng nó đã khiến cuộc sống của tôi dễ dàng hơn rất nhiều.
Tuyệt vời.
Mình cũng có tên trong danh sách mua một cái.
Tôi nóng lòng muốn bắt đầu sử dụng nó.
Số 41.""",
    },
    {
        "id": 63,
        "title": "Nap | Should | Take",
        "icon": "🎯",
        "file": "Q9.mp3",
        "en": """Listen and choose the correct answer.
I'm so tired.
A. I should take a nap.
B. You should take a nap.
C. He took a nap.""",
        "vi": """Nghe và chọn câu trả lời đúng.
Tôi mệt quá.
A. Tôi nên ngủ trưa.
B. Bạn nên ngủ trưa.
C. Anh ấy đã ngủ trưa.""",
    },
    {
        "id": 64,
        "title": "Haven | Office | Week",
        "icon": "📋",
        "file": "Q90-92.mp3",
        "en": """I haven't seen you in the office all week. Have you been following the recent business reports out of Asia?
No, I've been at a conference all week. I haven't had the time.
You might want to take a look at them. There are copies in the conference room. It might be a good idea to check them out before you start on anything else.
That sounds ominous. Something bad always happens when I leave the office for a few days.""",
        "vi": """Cả tuần nay tôi không thấy bạn ở văn phòng. Bạn có theo dõi các báo cáo kinh doanh gần đây ở Châu Á không?
Không, tôi đã dự hội nghị cả tuần rồi. Tôi chưa có thời gian.
Bạn có thể muốn xem xét chúng. Có những bản sao trong phòng họp. Có thể bạn nên kiểm tra chúng trước khi bắt đầu làm bất cứ điều gì khác.
Điều đó nghe có vẻ đáng ngại. Điều tồi tệ luôn xảy ra khi tôi rời văn phòng vài ngày.""",
    },
    {
        "id": 65,
        "title": "Results | Been | Maybe",
        "icon": "🎨",
        "file": "Q96-98.mp3",
        "en": """Maybe we should meet tomorrow to discuss the results of the market survey.
They've been gathering dust on my desk for weeks.
Yes, we've been procrastinating, haven't we?
I'd like to come up with a strategic plan for the year before the next quarter.
If we don't do it soon, it'll be too late.
Good.
How about at 10 in my office?
I'll print out the collated results for you.""",
        "vi": """Có lẽ ngày mai chúng ta nên gặp nhau để thảo luận về kết quả khảo sát thị trường.
Họ đã bám bụi trên bàn của tôi nhiều tuần rồi.
Vâng, chúng ta đã trì hoãn, phải không?
Tôi muốn đưa ra một kế hoạch chiến lược cho năm trước quý tiếp theo.
Nếu chúng ta không làm sớm thì sẽ quá muộn.
Tốt.
Thế còn lúc 10 giờ ở văn phòng của tôi thì sao?
Tôi sẽ in ra kết quả đối chiếu cho bạn.""",
    },
]

# 6. Sidebar bộ lọc bài nghe
st.sidebar.header("🔍 Lọc bài nghe")
search_term = st.sidebar.text_input("Tìm kiếm theo tên hoặc từ khóa:", "")

# 7. Vòng lặp hiển thị bài nghe
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

            # 8. Khung hiển thị Script & Dịch song song (Đã fix hoàn toàn lỗi hiển thị dịch)
         # Khung hiển thị Script & Dịch song song
         # Khung hiển thị Script & Dịch song song (Dùng HTML/JS để không giật lag audio)
           # Khung hiển thị Script & Dịch song song (Dùng HTML/JS để không giật lag audio)
           # Khung hiển thị Script & Dịch song song (SỬ DỤNG CSS THUẦN - TRỊ DỨT ĐIỂM LỖI STREAMLIT)
            with st.expander("📖 Hiển thị Script & Dịch nghĩa", expanded=False):
                # Ép xuống dòng chuẩn xác bằng thẻ HTML
                en_html = lesson['en'].replace('\n', '<br>')
                vi_html = lesson['vi'].replace('\n', '<br>')
                
                # KHÔNG thụt lề đoạn HTML này để tránh lỗi Markdown
                html_layout = f"""
<style>
/* 1. Ẩn hộp kiểm (checkbox) gốc */
.chk-hide-{lesson['id']} {{ display: none; }}

/* 2. Giao diện nút công tắc */
.btn-trans-{lesson['id']} {{
    cursor: pointer; font-family: sans-serif; font-size: 0.9rem; font-weight: 600; 
    color: #1d4ed8; background: #eff6ff; padding: 8px 18px; border-radius: 20px; 
    border: 1px solid #bfdbfe; float: right; margin-bottom: 12px; user-select: none;
    transition: 0.2s;
}}
.btn-trans-{lesson['id']}:hover {{ background: #dbeafe; }}

/* 3. Trạng thái cột Tiếng Việt: Mặc định là ẨN */
.col-vi-{lesson['id']} {{ display: none; flex: 1; min-width: 0; }}

/* 4. PHÉP THUẬT: Khi Checkbox bật -> Hiện cột Tiếng Việt */
.chk-hide-{lesson['id']}:checked ~ .content-row-{lesson['id']} .col-vi-{lesson['id']} {{ display: block; }}

/* 5. PHÉP THUẬT: Khi Checkbox bật -> Đổi màu nút sang Xanh lá */
.chk-hide-{lesson['id']}:checked + .btn-trans-{lesson['id']} {{
    background: #dcfce3; color: #15803d; border-color: #bbf7d0;
}}
</style>

<!-- Nút Bật/Tắt -->
<input type="checkbox" id="chk_{lesson['id']}" class="chk-hide-{lesson['id']}">
<label for="chk_{lesson['id']}" class="btn-trans-{lesson['id']}">🌐 Bật / Tắt Dịch Tiếng Việt</label>

<!-- Dọn dẹp khoảng trống của nút Float -->
<div style="clear: both;"></div>

<!-- Khung nội dung 2 cột -->
<div class="content-row-{lesson['id']}" style="display: flex; gap: 20px;">
    <!-- Cột Tiếng Anh -->
    <div style="flex: 1; min-width: 0;">
        <div style="color: #64748b; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; font-family: sans-serif;">🇺🇸 Tiếng Anh (Script):</div>
        <div class="script-box script-en">{en_html}</div>
    </div>
    
    <!-- Cột Tiếng Việt -->
    <div class="col-vi-{lesson['id']}">
        <div style="color: #64748b; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; font-family: sans-serif;">🇻🇳 Tiếng Việt (Dịch nghĩa):</div>
        <div class="script-box script-vi">{vi_html}</div>
    </div>
</div>
"""
                st.markdown(html_layout, unsafe_allow_html=True)

            st.divider()

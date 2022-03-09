import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

status = cycle(["한강물 온도시뮬레이션", "9개 서버에서 활동", "미잉 바보", "츠직츠직", "쭈그려서온도재기", "애플 키노트 만들기", "맛스타 해외승인"])

@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client = commands.Bot(command_prefix='한강봇 ')

@client.command()
async def test(ctx):
    await ctx.send('hello_world')

@client.command(aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
async def hellokor(ctx):
    await ctx.send('안녕하세요')

@client.command(aliases=['온도', '한강물온도', '한강수온', '오늘한강물', '물온도', '수온', '오늘한강', '오늘한강수온', '오늘수온', '오늘물온도'])
async def hangang(ctx):
    await ctx.send('절망은 희망의 단계일 뿐이다.너무 좌절하지 말라는 뜻. 7.2 °C 오후 11:00 업데이트')       

@client.command(aliases=['어쩔티비', 'ㅇㅉㅌㅂ', '어쩔', 'ㅇㅉ'])
async def azzal(ctx):
    await ctx.send('저쩔티비')  

@client.command(aliases=['저쩔티비', 'ㅈㅉㅌㅂ', '저쩔', 'ㅈㅉ'])
async def zazzal(ctx):
    await ctx.send('어쩔냉장고')  

@client.command(aliases=['개발자', '만든이', '만든사람', '아버지'])
async def mandene(ctx):
    await ctx.send('운하 EUN_NM-407#0645')  

@client.command(aliases=['감기엔', '감기', '치킨은', '치킨'])
async def chiken(ctx):
    await ctx.send('마늘 통닭')  

@client.command(aliases=['뭐하니', '뭐해', 'ㅁㅎ', '모해'])
async def whatareyoudoing(ctx):
    await ctx.send('강변북로에서 쭈그리고 물온도 재고 있어요!')  

@client.command(aliases=['공기공기공', 'ㄱㄱㄱㄱㄱ', '공기'])
async def air(ctx):
    await ctx.send('공기공기공 공기공기공~ 고무패킹을 갈지않으면 밥냄새는 돈 스탑 돈 스탑!')  

@client.command(aliases=['XOXO', '엑쏘엑쏘', '엑스오', '엑스오엑스오', '엑쏘'])
async def xoxo(ctx):
    await ctx.send('엣쏘엤쏘 디리리링 딩딩 디잉디잉~')  

@client.command(aliases=['전원입수', '눈딱감고낙하', '낙하', '입수'])
async def eapsu(ctx):
    await ctx.send('옙!------------------------------풍덩')  

@client.command(aliases=['채무자'])
async def takemoney(ctx):
    await ctx.send('장효주 돈 내놔')  

@client.command(aliases=['ㅁ ㅣ잉', '미잉', '요리'])
async def meing(ctx):
    await ctx.send('요리 고자')  

@client.command(aliases=['블로그', '명령어 목록', '사용법'])
async def howtouse(ctx):
    await ctx.send('제 블로그에요:https://hangangbotbyeunha.tistory.com/')

@client.command(aliases=['맛스타', '121687', '121687원', '맛스타 해외승인', '직불출금'])
async def matstar(ctx):
    await ctx.send('맛스타 해외승인 ~직불출금~ 십이만천육백팔십칠원!')

@client.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {client.user.name}")
    print(f"[!] 다음 : {client.user.id}")
    print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중\n")

    change_status.start()

client.run('OTQyMDExMzc5MjY5OTE4NzMx.YgeSdg.wG5KPRweu_opPH3BcQ-y22s7EMg')
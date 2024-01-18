# 기억한 멜로디 - 재생 시간, 제공 악보 직접 비교
# 음악 제목, 재생 시작, 종료 시간, 악보
def change(melody):
    if 'A#' in melody: melody = melody.replace('A#','a')
    if 'C#' in melody: melody = melody.replace('C#','c')
    if 'D#' in melody: melody = melody.replace('D#','d')
    if 'F#' in melody: melody = melody.replace('F#','f')
    if 'G#' in melody: melody = melody.replace('G#','g')
    return melody

def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', None)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        melody = change(melody)

        hour1, minute1 = map(int, start.split(':'))
        hour2, minute2 = map(int, end.split(':'))
        time = 60*(hour2-hour1) + (minute2-minute1)

        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] is None) or (time > answer[1]):
                answer = (title, time)
                
    return answer[0]

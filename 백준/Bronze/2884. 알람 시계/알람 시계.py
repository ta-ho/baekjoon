h_sang, m_sang = map(int, input().split())
total_m_sang = h_sang * 60 + m_sang
total_m_chang = total_m_sang - 45

print((total_m_chang // 60) % 24, total_m_chang % 60)
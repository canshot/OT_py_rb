puts("아이디를 입력해주세요")
input_id = gets.chomp()
puts("비밀번호를 입력해주세요")
input_pw = gets.chomp()
real_id = "egoin"
real_pw = "11"
if real_id == input_id
  if real_pw == input_pw
    puts("Hello!")
  else
    puts("잘못된 비밀번호입니다")
  end
else
  puts("잘못된 아이디입니다")
end

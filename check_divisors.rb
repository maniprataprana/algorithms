

t = gets.chomp
N = t.to_i
$TTT = gets.chomp
S = $TTT.split(" ").map { |x| x.to_i }

$i = 0
$answer = ""
while $i < N  do
   $num = S[$i]
   $j = 0
   $found = 0
   while $j < N do
		if S[$j] != S[$i] && S[$i] % S[$j] == 0
         $found = 1
         break
      end
      $j =$j + 1
   end
   if $found == 0
      $answer = $answer+"#{S[$i]} "
   end

   $i = $i+ 1
end
puts $answer
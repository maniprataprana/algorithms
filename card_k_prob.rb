

t = gets.chomp
T = t.to_i

$i = 0

while $i < T  do
   $TTT = gets.chomp
   $TT = $TTT.split(" ")
   $X = $TT[0].to_i
   $N = $TT[1].to_i
   $D = $TT[2].to_i
   $K = $TT[3]

   $j = $X
   $mul = $X
   while $j < $N do
   		$mul = $mul * $j
   		$j = $j - 1 
   end

   $r = (1.0/$mul.to_i)

   puts "%.10f" % $r

   $i +=1
end
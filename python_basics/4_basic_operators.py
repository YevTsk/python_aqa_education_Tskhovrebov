x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(f'x_list contains  {len (x_list)} objects')
print("x_list contains %d objects" % len(x_list))

print(f'y_list contains  {len (y_list)} objects')
print("y_list contains %d objects" % len(y_list))

print(f'big_list contains  {len (big_list)} objects')
print("big_list contains %d objects" % len(big_list))

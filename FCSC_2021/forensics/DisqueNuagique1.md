The description is asking for the offset of partition of UUID
e61a1da4-b95d-4df5-ab40-bbffc505b3f2

We have a ewf disk

```bash
mkdir rawimage
sudo ewfmount disque.e01 ./rawimage/
```

Then looking at `fdisk -l` we see two partitions

```
Disk rawimage/ewf1: 10 GiB, 10737418240 bytes, 20971520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xb69e7b6d

Device          Boot   Start      End  Sectors  Size Id Type
rawimage/ewf1p1 *       2048   999423   997376  487M 83 Linux
rawimage/ewf1p2      1001470 20969471 19968002  9.5G  5 Extended
rawimage/ewf1p5      1001472 20969471 19968000  9.5G 83 Linux
```

I extracted the second one with `dd`.

```bash
sudo dd if=rawimage/ewf1 of=/mnt/part skip=1001472
```

We run `file` to verify its UUID

```
$ file /mnt/part 
/mnt/part: LUKS encrypted file, ver 2 [, , sha256] UUID: e61a1da4-b95d-4df5-ab40-bbffc505b3f2
```

So the offset was 1001472*512 

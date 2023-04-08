# apply_noise_filter_multiprocessing
apply noise filter to an image using multiprocessing

### uning multiprocessing
```bash
$ python apply_noise_filter_mp.py .
Starting image processing of 5 images...
Processed img1_noisy.jpg (1/5, 0.00% complete)
Processed IMG2_noisy.jpg (2/5, 20.00% complete)
Processed IMG3_noisy.png (3/5, 40.00% complete)
Processed img4_noisy.jpg (4/5, 60.00% complete)
Processed img5_noisy.jpg (5/5, 80.00% complete)
Processing complete! 5 images processed in 16.10 seconds.
```

### not using multiprocessing
```bash
$ python apply_noise_filter_not_mp.py .
Starting image processing of 5 images...
Processed img1_noisy.jpg (1/5, 0.00% complete)
Processed IMG2_noisy.jpg (2/5, 20.00% complete)
Processed IMG3_noisy.png (3/5, 40.00% complete)
Processed img4_noisy.jpg (4/5, 60.00% complete)
Processed img5_noisy.jpg (5/5, 80.00% complete)
Processing complete! 5 images processed in 59.08 seconds.
```

# RANLP2021-Anonymous sumbission
Submission repository to the RANLP 2021 conference

## Build and run the project
### Build
`docker build -t "SADPGAN" . | tee log`

### Train SADPGAN
`docker run --gpus all --rm -v <projecthome>/Anonymous/src/run/ SADPGAN bash -c "cd /app && python -m run_sa_dpgan.py 1 2"`

### Train DPGAN
`docker run --gpus all --rm -v <projecthome>/Anonymous/src/run/ DPGAN bash -c "cd /app && python -m run_dpgan.py 1 2"`

## Original repo
https://github.com/williamSYSU/TextGAN-PyTorch

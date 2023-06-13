<!-- Title -->
<h1 align="center"><b>Facebook Post Crawler</b></h1>

## Set up environment

```
conda env create -f environment.yml
conda activate webcrawling
```

## Crawl
To crawl posts and comments from a facebook page, you can run the following command

```
python main.py --page <Facebook Page ID> --headless
```


import filters
import panflute as pf


def main(doc=None):
    return(pf.run_filters([filters.decrement_headers, filters.fix_local_links], doc=doc))


if __name__ == '__main__':
    main()

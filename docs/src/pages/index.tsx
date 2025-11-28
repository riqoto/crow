import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className="hero">
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/intro">
            Get Started
          </Link>
          <Link
            className="button button--secondary button--lg margin-left--md"
            to="/docs/api/overview">
            View API
          </Link>
        </div>
      </div>
    </header>
  );
}

type FeatureItem = {
  title: string;
  icon: string;
  description: React.JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Multi-Format Support',
    icon: '📊',
    description: (
      <>
        Crow supports multiple data formats including CSV, Excel (XLSX/XLS),
        JSON, and TXT files. Load and analyze data from any source with a
        unified interface.
      </>
    ),
  },
  {
    title: 'Statistical Analysis',
    icon: '🧮',
    description: (
      <>
        Perform essential statistical calculations like mean, variance, and
        median on your datasets. Built on top of pandas for reliable and
        efficient data processing.
      </>
    ),
  },
  {
    title: 'Simple & Clean API',
    icon: '🚀',
    description: (
      <>
        Intuitive API design makes it easy to get started. Load your data,
        run your analysis, and get results in just a few lines of code.
      </>
    ),
  },
];

function Feature({ title, icon, description }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="feature">
        <div className="feature__icon">{icon}</div>
        <Heading as="h3" className="feature__title">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): React.JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} - Statistical Analysis Library`}
      description="A Python library for statistical analysis across multiple data formats">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}

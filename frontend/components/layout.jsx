import Head from "next/head";

import styles from "./layout.module.css";

const Layout = ({ children }) => {
  return (
    <>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet" />
      </Head>
      <div className={styles.container}>{children}</div>
    </>
  );
};

export default Layout;

import Head from "next/head";

import styles from "./layout.module.css";

const Layout = ({ className = "", children }) => {
  return (
    <>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet" />
      </Head>
      <div className={styles.container}>{children}</div>
    </>
  );
};

export default Layout;

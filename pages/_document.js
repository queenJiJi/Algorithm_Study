// pages/_document.js
import Document, { Html, Head, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html lang="en">
        <Head>
          {/* SEO 적용 */}
          <title>StudyDate - Connect with Study Partners</title>
          <meta name="description" content="Find and connect with study mates who share your interests and goals." />
          <meta name="author" content="JiJi StudyDate" />
          <meta property="og:title" content="StudyDate - Find Your Study/Date Mate" />
          <meta property="og:description" content="StudyDate helps you find study member or date mate who match your goals." />
          <meta property="og:image" content="/assets/studydate_logo.png" />
          <meta property="og:url" content="https://www.Ji-studydate.com/" />
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
          <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;